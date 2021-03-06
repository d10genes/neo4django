def setup():
    global neo4django, neo4jrestclient, gdb, Person, settings, neo_constants
    global models

    from django.conf import settings

    import neo4django, neo4jrestclient.client as neo4jrestclient
    from neo4django.db import models
    from neo4django.db import connection as gdb
    import neo4jrestclient.constants as neo_constants

    class Person(models.NodeModel):
        name = models.Property()
        age = models.IntegerProperty(indexed=True)
