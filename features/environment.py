import os
import shutil


def after_scenario(context, scenario):
    if hasattr(context, "work_dir") and os.path.exists(context.work_dir):
        shutil.rmtree(context.work_dir)
