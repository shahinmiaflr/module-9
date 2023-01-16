def wp_paragraph(p_text):
    '''
    It will take normal text as input and return wp block editor code
    :param p_text: take normal text
    :return: wp block editor paragraph text
    '''
    code = f"<!-- wp:paragraph --><p>{p_text}</p><!-- /wp:paragraph -->"
    return code
# pg = wp_paragraph('this is text for paragraph')
# print(pg)

def wp_h2(heading_text):
    '''
    It will return wordpress block editor code
    :param heading_text: take palain text
    :return: output will be WP block editor code
    '''
    code = f"<!-- wp:heading --><h2>{heading_text}</h2><!-- /wp:heading -->"
    return code
