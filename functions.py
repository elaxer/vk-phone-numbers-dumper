from config import FILTERS


def phone_filter(phone):
    return phone != '' \
           and sum(d.isdigit() for d in phone) >= FILTERS['min_digits_count'] \
           and phone not in FILTERS['ignored_phones']


def write_phone(user, f):
    f.write('{} {}(https://vk.com/id{}): {}\n'.format(
        user['first_name'],
        user['last_name'],
        user['id'],
        user['mobile_phone'])
    )
