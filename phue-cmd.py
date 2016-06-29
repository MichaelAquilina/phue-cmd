import os
import sys

from phue import Bridge


def list_lights(bridge):
    for light_id, light in bridge.get_api()['lights'].items():
        print('{light_id}: {light_name} [{light_state}]'.format(
            light_id=light_id,
            light_name=light['name'],
            light_state=('on' if light['state']['on'] else 'off'),
        ))


def set_light_attribute(bridge, light_ids, key, value):
    bridge.set_light(light_ids, key, value)


def get_bridge_ip_addr():
    with open(os.path.expanduser('~/.phue'), 'r') as fp:
        bridge_addr = fp.read().strip()
    return bridge_addr


def main():
    bridge_addr = get_bridge_ip_addr()
    bridge = Bridge(bridge_addr)
    bridge.connect()

    if sys.argv[1] == 'set':
        set_light_attribute(bridge, [1, 3], sys.argv[2], int(sys.argv[3]))


if __name__ == '__main__':
    main()
