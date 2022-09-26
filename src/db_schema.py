from sqlalchemy_schemadisplay import create_schema_graph
from sqlalchemy import MetaData
from config import Config

config = Config()
graph = create_schema_graph(
    metadata=MetaData(config.SQLALCHEMY_DATABASE_URI),
    show_datatypes=False, # The image would get nasty big if we'd show the datatypes
    show_indexes=False, # ditto for indexes
    rankdir='LR', # From left to right (instead of top to bottom)
    concentrate=False # Don't try to join the relation lines together
)
graph.set('scale', 2)
graph.write_png('./db_schema.png')
