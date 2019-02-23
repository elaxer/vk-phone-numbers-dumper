import vk
import sys
import config
import functions


def main():
    api = vk.API(vk.Session(access_token=config.TOKEN), v=config.VERSION)

    arguments = sys.argv[1:]
    group_id = arguments[0]

    try:
        group = api.groups.getMembers(group_id=group_id)
    except vk.exceptions.VkAPIError as e:
        exit(e)

    count = group['count']
    offset = 0

    file_name = config.DUMP_DIRECTORY + '/' + group_id + '.txt'
    f = open(file_name, 'w')

    phones_count = 0
    while offset < count:
        members = api.groups.getMembers(group_id=group_id, offset=offset)['items']
        users = api.users.get(user_ids=members, fields=('contacts', 'is_closed'))

        for user in users:
            if 'mobile_phone' in user and functions.phone_filter(user['mobile_phone']):
                phones_count += 1
                print('Got ' + str(phones_count) + ' phone numbers')

                functions.write_phone(user, f)

        print('Analysed {} of {} users'.format(offset, count))

        offset += 1000

    print('Analysed {} of {} users'.format(count, count))
    f.close()


if __name__ == '__main__':
    main()
