def quote_plus(v):
    # TODO
    return v


def IS_STR(v):
    # TODO
    return True


def _url(**db_parameters):
    """
    Composes a SQLAlchemy connect string from the given database connection
    parameters.
    """
    specified_parameters = []

    if "host" in db_parameters:
        ret = "omnisci://{user}:{password}@{host}:{port}/".format(
            user=db_parameters["user"],
            password=quote_plus(db_parameters["password"]),
            host=db_parameters["host"],
            port=db_parameters["port"] if "port" in db_parameters else 6274,
        )
        specified_parameters += ["user", "password", "host", "port"]
        specified_parameters += ["user", "password", "account"]

    if "database" in db_parameters:
        ret += quote_plus(db_parameters["database"])
        specified_parameters += ["database"]

    def sep(is_first_parameter):
        return "?" if is_first_parameter else "&"

    is_first_parameter = True
    for p in sorted(db_parameters.keys()):
        v = db_parameters[p]
        if p not in specified_parameters:
            encoded_value = quote_plus(v) if IS_STR(v) else str(v)
            ret += sep(is_first_parameter) + p + "=" + encoded_value
            is_first_parameter = False
    return ret
