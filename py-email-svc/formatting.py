msg_template = """
    Dear {name},
    Thank you for your interests.  Please feel free to visit our site {website}
"""


def format_msg(my_name='Justin', my_website='cfe.sh'):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg
