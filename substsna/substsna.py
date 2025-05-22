def mkarango(dbase):
    import configparser
    import sys
    from arango import ArangoClient
    sysconf = configparser.ConfigParser()
    sysconf.read('/Users/brain/.SubstackSNA/substsna.conf')
    try:
       client = ArangoClient(hosts=sysconf['SYSTEM']['arangourl'])
    except (RuntimeError, TypeError, NameError) as prob:
        print(prob)
        sys.exit()
    db = client.db(dbase, username=sysconf['SYSTEM']['arangouser'], password=sysconf['SYSTEM']['arangopass'])
    return(db)