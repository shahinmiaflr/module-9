import wp_function
first_para = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."

first_heading_text = "Why do we use it?"

second_para = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."

article = wp_function.wp_paragraph(first_para)+wp_function.wp_h2(first_heading_text)+wp_function.wp_paragraph(second_para)
print(article)