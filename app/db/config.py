#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class todotable:

    NAME = "todotable"

    SCHEMA = """
        CREATE TABLE todotable (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            priority   INTEGER NOT NULL DEFAULT 3,
            COMPLETE INTEGER NOT NULL DEFAULT 0
        )
    """

    SEED_DATA = """
        INSERT INTO todotable (name, priority)
        VALUES
            ("Pippa"),
            ("Barry"),
            ("Helen")
    """

# Add more table classes here...



#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1,
#     Table2,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
#       foreign keys AFTER the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    todotable,
    # Add more tables here...
]

