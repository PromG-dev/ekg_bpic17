from colorama import Fore

from module_manager import ModuleManager

from colorama import Fore
from promg import OcedPg, SemanticHeader, DatasetDescriptions
from promg.modules.db_management import DBManagement
from promg.modules.task_identification import TaskIdentification

from custom_modules.custom_modules.delay_analysis import PerformanceAnalyzeDelays
from custom_modules.custom_modules.df_interactions import InferDFInteractions
from custom_modules.custom_modules.discover_dfg import DiscoverDFG


class MethodManager:
    def __init__(self, config=None):
        self.modules = ModuleManager(config=config)

    def clear_database(self):
        db_manager = self.modules.get_db_manager()
        print(Fore.RED + 'Clearing the database.' + Fore.RESET)
        db_manager.clear_db(replace=True)
        db_manager.set_constraints()

    def load_and_transform_records(self):
        if self.modules.get_is_preprocessed_files_used():
            print(Fore.RED + '💾 Preloaded files are used!' + Fore.RESET)
        else:
            print(Fore.RED + '📝 Importing and creating files' + Fore.RESET)

        oced_pg = self.modules.get_oced_pg()
        oced_pg.load_and_transform()
        oced_pg.create_df_edges()

    def finish_and_save(self):
        performance = self.modules.get_performance()
        performance.finish_and_save()

    def print_statistics(self):
        db_manager = self.modules.get_db_manager()
        db_manager.print_statistics()

    def infer_delays(self):
        print(Fore.RED + 'Computing delay edges.' + Fore.RESET)
        delays = self.modules.get_performance_analysis_delay_module()
        delays.enrich_with_delay_edges()
        delays.analyze_delays()
        delays.visualize_delays(10000)

    def build_tasks(self):
        print(Fore.RED + 'Detecting tasks.' + Fore.RESET)
        task_identifier = self.modules.get_task_identifier_module(
            resource="Resource",
            case="CaseAWO")
        task_identifier.identify_tasks()
        task_identifier.aggregate_on_task_variant()

    def discover_model(self):
        print(Fore.RED + 'Discovering multi-object DFG.' + Fore.RESET)
        dfg = self.modules.get_discover_dfg_module()
        dfg.discover_dfg_for_entity("Application", 25000, 0.0)
        dfg.discover_dfg_for_entity("Offer", 25000, 0.0)
        dfg.discover_dfg_for_entity("Workflow", 25000, 0.0)
        dfg.discover_dfg_for_entity("CASE_AO", 25000, 0.0)
        dfg.discover_dfg_for_entity("CASE_AW", 25000, 0.0)
        dfg.discover_dfg_for_entity("CASE_WO", 25000, 0.0)

    def delete_parallel_df(self):
        print(Fore.RED + 'Inferring DF over relations between objects.' + Fore.RESET)
        infer_df_interactions = self.modules.get_infer_df_interactions_module()
        infer_df_interactions.delete_parallel_directly_follows_derived('CASE_AO', 'Application')
        infer_df_interactions.delete_parallel_directly_follows_derived('CASE_AO', 'Offer')
        infer_df_interactions.delete_parallel_directly_follows_derived('CASE_AW', 'Application')
        infer_df_interactions.delete_parallel_directly_follows_derived('CASE_AW', 'Workflow')
        infer_df_interactions.delete_parallel_directly_follows_derived('CASE_WO', 'Workflow')
        infer_df_interactions.delete_parallel_directly_follows_derived('CASE_WO', 'Offer')
