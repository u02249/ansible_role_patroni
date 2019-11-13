#!/usr/bin/env python

import logging
import sys

logger = logging.getLogger(__name__)


class EvenHandler(object):

    def __init__(self, ip, eth_name):
        self.add_address_cmd = "ip addr add {ip} dev {dev}".format(ip=ip, dev=eth_name)
        self.del_address_cmd = "ip addr del {ip} dev {dev}".format(ip=ip, dev=eth_name)
        self.arping_cmd = "arping -q -c 3 -A -I {dev} {ip}".format(ip=ip, dev=eth_name)

    def add_ip():
        os.system(self.add_address_cmd)
        os.system(self.arping_cmd)

    def del_ip():
        os.system(self.del_address_cmd)

    def on_role_change(self, new_role):
        try:
            if new_role == "master":
                self.add_ip()
            else:
                self.del_ip()
            
        except:
            logger.warning("Проблема с установкой IP")
            return False
        return True


def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)
    ip = 10.128.0.7/32
    eth_name = {{patroni_dev_name}}
    if len(sys.argv) == 4 and sys.argv[1] in ('on_start', 'on_stop', 'on_role_change'):
        EvenHandler(ip, eth_name).on_role_change(sys.argv[2])
    else:
        sys.exit("Usage: {0} action role name".format(sys.argv[0]))


if __name__ == '__main__':
    main()