from fabric import Connection
from pack_web_static import Fabfile

cxn = Connection('localhost')
fabfile = Fabfile(cxn)
print(fabfile.do_pack())
