from datetime import datetime
from method_manager import MethodManager

step_clear_db = True
step_populate_graph = True
step_delete_parallel_df = False
step_discover_model = False
step_build_tasks = False
step_infer_delays = False


def main() -> None:
    """
    Main function, read all the logs, clear and create the graph, perform checks
    @return: None
    """
    print("Started at =", datetime.now().strftime("%H:%M:%S"))

    methods = MethodManager()

    if step_clear_db:
        methods.clear_database()

    if step_populate_graph:
        methods.load_and_transform_records()

    if step_delete_parallel_df:
        methods.delete_parallel_df()

    if step_discover_model:
        methods.discover_model()

    if step_build_tasks:
        methods.build_tasks()

    if step_infer_delays:
        methods.infer_delays()

    methods.finish_and_save()
    methods.print_statistics()


if __name__ == "__main__":
    main()
