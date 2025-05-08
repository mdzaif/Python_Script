# script for create html signature for email account
# Use only for company mail.
# download this file then run python3 <this_file_name>


name = input("Enter your name: ")
position = input("Enter your position: ")
company_name = input("Enter your compnay name: ")
mail=input("Enter the your email: ").strip()
country_code = input("Enter the country code: ").strip()
number = input("Enter your number here avoid the country code here: ").strip()
address = input("Enter your address: ")
web_link = input("Enter your website link: ").strip()
web_logo = input("Enter your web site logo link: ").strip()
facebook_link = input("Enter your company facebok link: ").strip()
linkedin_link = input("Enter your linkedin link: ").strip()
x_link = input("Enter your x link: ").strip()

file = open("mail_sign_temp.txt", "r")
text = file.read()

html_file = text.format(name=name,
                        position=position,
                        company_name=company_name,
                        mail=mail,
                        country_code=country_code,
                        number=number,
                        address=address,
                        web_link=web_link,
                        web_logo=web_logo,
                        facebook_link=facebook_link,
                        linkedin_link=linkedin_link,
                        x_link=x_link
                        )

with open(f"{mail}.html", "w") as file:
    file.write(html_file)
