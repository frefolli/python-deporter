from dotenv import dotenv_values

def get_env_or_default(
        environment_variable: str,
        default_value: str) -> str:
    config = dotenv_values('.env')
    value = (config.get(environment_variable) if config.get(environment_variable) is not None else default_value)
    return value

def get_env_or_raise(
        environment_variable: str):
    res = get_env_or_default(environment_variable, None)
    if res is None:
        raise Exception("enviroment variable %s is not set properly" %
                        environment_variable)
    return res
