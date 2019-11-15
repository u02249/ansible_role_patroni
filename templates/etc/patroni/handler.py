#!/usr/bin/env python
import logging
import sys
import os

logger = logging.getLogger(__name__)

class EvenHandler(object):

    def add_ip(self):
        logger.warning("add ip {{patroni_add_ip_cmd}}")
        os.system("sudo {{patroni_add_ip_cmd}}")
        os.system("sudo {{patroni_arping_cmd}}")

    def del_ip(self):
        logger.warning("del ip {{patroni_del_ip_cmd}}")
        os.system("sudo {{patroni_del_ip_cmd}}")

    def on_role_change(self, new_role):
        logger.warning("---------------------------------->" + new_role)
        try:
            if new_role == "master":
                self.add_ip()
            else:
                self.del_ip()
        except:
            logger.warning("Error to change ip")
            return False
        return True

def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)
    if len(sys.argv) == 4 and sys.argv[1] in ('on_start', 'on_stop', 'on_role_change'):
        EvenHandler().on_role_change(sys.argv[2])
    else:
        sys.exit("Usage: {0} action role name".format(sys.argv[0]))

if __name__ == '__main__':
    main()