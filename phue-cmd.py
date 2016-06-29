import argparse
import os

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
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest='command')

    power_parser = subparsers.add_parser('power', help='set lights to on or off state')
    power_parser.add_argument('state', choices=('on', 'off'))

    parser.add_argument('--light', type=int)

    bridge_addr = get_bridge_ip_addr()
    bridge = Bridge(bridge_addr)
    bridge.connect()

    args = parser.parse_args()

    if args.command == 'power':
        set_light_attribute(bridge, args.light, 'on', args.state == 'on')


if __name__ == '__main__':
    main()
