from promg import SemanticHeader, OcedPg
from promg import DatabaseConnection
from promg import DatasetDescriptions

from promg import Performance
from promg.modules.db_management import DBManagement
from promg import Configuration
from promg.modules.task_identification import TaskIdentification

from custom_modules.custom_modules.delay_analysis import PerformanceAnalyzeDelays
from custom_modules.custom_modules.df_interactions import InferDFInteractions
from custom_modules.custom_modules.discover_dfg import DiscoverDFG


class ModuleManager:
    def __init__(self, config):
        if config is None:
            config = Configuration.init_conf_with_config_file()
        self._config = config
        self._db_connection = DatabaseConnection.set_up_connection(config=config)
        self._performance = Performance.set_up_performance(config=config)
        self._semantic_header = SemanticHeader.create_semantic_header(config=config)
        self._dataset_descriptions = DatasetDescriptions(config=config)

        self._db_manager = None
        self._oced_pg = None
        self._performance_analysis_delay_module = None
        self._task_identifier = None
        self._discover_dfg_module = None
        self._infer_df_interactions_module = None

    def get_config(self):
        return self._config

    def get_is_preprocessed_files_used(self):
        return self._config.use_preprocessed_files

    def get_db_connection(self):
        return self._db_connection

    def get_performance(self):
        return self._performance

    def get_db_manager(self):
        if self._db_manager is None:
            self._db_manager = DBManagement(db_connection=self._db_connection)
        return self._db_manager

    def get_oced_pg(self):
        if self._oced_pg is None:
            self._oced_pg = OcedPg(database_connection=self._db_connection,
                                   dataset_descriptions=self._dataset_descriptions,
                                   semantic_header=self._semantic_header,
                                   use_sample=self._config.use_sample,
                                   use_preprocessed_files=self._config.use_preprocessed_files)
        return self._oced_pg

    def get_performance_analysis_delay_module(self):
        if self._performance_analysis_delay_module is None:
            self._performance_analysis_delay_module = PerformanceAnalyzeDelays(db_connection=self._db_connection)
        return self._performance_analysis_delay_module

    def get_task_identifier_module(self, resource="Resource", case="CaseAWO"):
        if self._task_identifier is None:
            self._task_identifier = TaskIdentification(
                db_connection=self._db_connection,
                semantic_header=self._semantic_header,
                resource=resource,
                case=case)
        return self._task_identifier

    def get_discover_dfg_module(self):
        if self._discover_dfg_module is None:
            self._discover_dfg_module = DiscoverDFG(db_connection=self._db_connection,
                                                    semantic_header=self._semantic_header)
        return self._discover_dfg_module

    def get_infer_df_interactions_module(self):
        if self._infer_df_interactions_module is None:
            self._infer_df_interactions_module = InferDFInteractions(db_connection=self._db_connection,
                                                                     semantic_header=self._semantic_header)
        return self._infer_df_interactions_module
