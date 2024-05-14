from dotenv import dotenv_values
import logging
import os

def get_env_or_default(
        environment_variable: str,
        default_value: str) -> str:
    config_dir = os.path.expanduser('~/.config/python-deporter')
    if not os.path.exists(config_dir):
        logging.debug("Creating config_dir: '%s'" % config_dir)
        os.system("mkdir -p %s" % config_dir)
    config_db_path = os.path.join(config_dir, "secrets")
    config = dotenv_values(config_db_path)
    value = (config.get(environment_variable) if config.get(environment_variable) is not None else default_value)
    return value

def get_env_or_raise(
        environment_variable: str):
    res = get_env_or_default(environment_variable, None)
    if res is None:
        raise Exception("enviroment variable %s is not set properly" %
                        environment_variable)
    return res
