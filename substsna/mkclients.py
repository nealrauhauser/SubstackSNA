def mkarango(dbase):

    sysconf = configparser.ConfigParser()
    sysconf.read('~/.SubstackSNA/substsna.conf')
    try:
       client = ArangoClient(hosts=sysconf['SYSTEM']['arangourl'])
    except (RuntimeError, TypeError, NameError) as prob:
        print(prob)
        sys.exit()
    db = client.db(dbase, username=sysconf['SYSTEM']['arangouser'], password=sysconf['SYSTEM']['arangopass'])
    return(db)