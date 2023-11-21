#!/usr/bin/env python
# coding: utf-8

# ### python에서 bigquery 접속하기

# In[1]:


get_ipython().system('pip install google-cloud-bigquery google-auth db-dtypes')


# In[2]:


from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('./data/key1.json')


# In[3]:


from google.cloud import bigquery

client = bigquery.Client(
    credentials=credentials, 
    project=credentials.project_id
)


# In[32]:


sql = "SELECT COUNT(*) AS cnt FROM `pacific-castle-404708.project1.pets`"


# In[33]:


df = client.query(sql).to_dataframe()
df


# In[60]:


# 1) 2019~2022 -> 서울시 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28,
FROM 
   project1.pets
WHERE
   string_field_0 = "서울시"
"""


# In[61]:


df = client.query(sql).to_dataframe()
df


# In[52]:


# 1) 2019~2022 -> 서울시 -> 반려동물 유무 -> 없다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_3,
   string_field_11,
   string_field_20,
   string_field_29
FROM 
   project1.pets
WHERE
   string_field_0 = "서울시"
"""


# In[53]:


df = client.query(sql).to_dataframe()
df


# In[54]:


# import seaborn as sns


# In[1]:


# 1) 2019~2022 -> 서울시 -> 반려동물 유무 -> 있다
# 1) 2019~2022 -> 서울시 -> 반려동물 유무 -> 없다
# 그래프 합치기

import matplotlib.pyplot as plt

# Data for the first line graph
x_values1 = [2019, 2020, 2021, 2022]
y_values1 = [20.1, 20.0, 19.6, 22.2]

# Data for the second line graph
x_values2 = [2019, 2020, 2021, 2022]
y_values2 = [79.9, 80.0, 80.4, 77.8]

# Create two line graphs
plt.plot(x_values1, y_values1, marker='o', linestyle='-', color='blue', label='Yes')
plt.plot(x_values2, y_values2, marker='s', linestyle='--', color='green', label='No')

# Adding labels and title
plt.xlabel('Years')
plt.ylabel('Values(%)')
plt.title('Seoul, "Do you have pet(s)? Yes or No"')

# Adding a legend
plt.legend()

# Display the line graphs
plt.show()


# In[117]:


# 2) 2019~2022 -> 성별(여자) -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "성별" AND
   string_field_1 = "여성"
"""


# In[118]:


df = client.query(sql).to_dataframe()
df


# In[49]:


# 2) 2019~2022 -> 성별(여자) -> 반려동물 유무 -> 있다

import matplotlib.pyplot as plt

# Data for the bar graph
categories = ['2019', '2020', '2021', '2022']
values = [23.9, 20.2, 18.9, 20.8]

# Create a bar graph
plt.bar(categories, values, color='blue', width=0.5)

# Adding labels and title
plt.xlabel('Years')
plt.ylabel('Values(%)')
plt.title('Women, "have pet(s)"')

# Display the bar graph
plt.show()


# In[119]:


# 2) 2019~2022 -> 성별(남자) -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28,
FROM 
   project1.pets
WHERE
   string_field_0 = "성별" AND
   string_field_1 = "남성"
"""


# In[120]:


df = client.query(sql).to_dataframe()
df


# In[48]:


# 2) 2019~2022 -> 성별(남자) -> 반려동물 유무 -> 있다

import matplotlib.pyplot as plt

# Data for the bar graph
categories = ['2019', '2020', '2021', '2022']
values = [18.7, 19.9, 20.0, 22.8]

# Create a bar graph
plt.bar(categories, values, color='green', width=0.5)

# Adding labels and title
plt.xlabel('Years')
plt.ylabel('Values(%)')
plt.title('Men, "have pet(s)"')

# Display the bar graph
plt.show()


# In[4]:


# 2) 2019~2022 -> 성별(여자) -> 반려동물 유무 -> 없다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_3,
   string_field_11,
   string_field_20,
   string_field_29
FROM 
   project1.pets
WHERE
   string_field_0 = "성별" AND
   string_field_1 = "여성"
"""


# In[8]:


df = client.query(sql).to_dataframe()
df


# In[47]:


import matplotlib.pyplot as plt

# Data for the bar graph
categories = ['2019', '2020', '2021', '2022']
values = [76.1, 79.8, 81.1, 79.2]

# Create a bar graph
plt.bar(categories, values, color='blue', width=0.5)

# Adding labels and title
plt.xlabel('Years')
plt.ylabel('Values(%)')
plt.title('Women, "no pet"')

# Display the bar graph
plt.show()


# In[9]:


# 2) 2019~2022 -> 성별(남자) -> 반려동물 유무 -> 없다

sql = """
SELECT  
string_field_0,
   string_field_1,
   string_field_3,
   string_field_11,
   string_field_20,
   string_field_29
FROM 
   project1.pets
WHERE
   string_field_0 = "성별" AND
   string_field_1 = "남성"
"""


# In[10]:


df = client.query(sql).to_dataframe()
df


# In[46]:


import matplotlib.pyplot as plt

# Data for the bar graph
categories = ['2019', '2020', '2021', '2022']
values = [81.3, 80.1, 80.0, 77.2]

# Create a bar graph
plt.bar(categories, values, color='green', width=0.5)

# Adding labels and title
plt.xlabel('Years')
plt.ylabel('Values(%)')
plt.title('Men, "no pet"')

# Display the bar graph
plt.show()


# In[28]:


# 3) 2019~2022 -> 연령별(20대 이하, 30대, 40대, 50대, 60세 이상) 20대 이하 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "연령별" AND
   string_field_1 = "20대 이하"
"""


# In[29]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[30]:


# 3) 2019~2022 -> 연령별(20대 이하, 30대, 40대, 50대, 60세 이상) 30대 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "연령별" AND
   string_field_1 = "30대"
"""


# In[31]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[32]:


# 3) 2019~2022 -> 연령별(20대 이하, 30대, 40대, 50대, 60세 이상) 40대 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "연령별" AND
   string_field_1 = "40대"
"""


# In[33]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[34]:


# 3) 2019~2022 -> 연령별(20대 이하, 30대, 40대, 50대, 60세 이상) 50대 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "연령별" AND
   string_field_1 = "50대"
"""


# In[35]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[38]:


# 3) 2019~2022 -> 연령별(20대 이하, 30대, 40대, 50대, 60세 이상) 60세 이상 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "연령별" AND
   string_field_1 = "60세 이상"
"""


# In[39]:


df = client.query(sql).to_dataframe()
df


# In[45]:


# 3) 2019~2022 -> 연령별(20대 이하, 30대, 40대, 50대, 60세 이상) 20대 이하 -> 반려동물 유무 -> 있다
# 3) 2019~2022 -> 연령별(20대 이하, 30대, 40대, 50대, 60세 이상) 30대 -> 반려동물 유무 -> 있다
# 3) 2019~2022 -> 연령별(20대 이하, 30대, 40대, 50대, 60세 이상) 40대 -> 반려동물 유무 -> 있다
# 3) 2019~2022 -> 연령별(20대 이하, 30대, 40대, 50대, 60세 이상) 50대 -> 반려동물 유무 -> 있다
# 3) 2019~2022 -> 연령별(20대 이하, 30대, 40대, 50대, 60세 이상) 60세 이상 -> 반려동물 유무 -> 있다
# 그래프 합치기

import matplotlib.pyplot as plt

# Data for the first line graph
x_values1 = [2019, 2020, 2021, 2022]
y_values1 = [20.4, 17.7, 16.3, 20.0]

# Data for the second line graph
x_values2 = [2019, 2020, 2021, 2022]
y_values2 = [20.5, 19.1, 19.6, 20.0]

# Data for the third line graph
x_values3 = [2019, 2020, 2021, 2022]
y_values3 = [19.6, 21.9, 20.3, 24.2]

# Data for the fourth line graph
x_values4 = [2019, 2020, 2021, 2022]
y_values4 = [21.6, 24.2, 22.4, 24.8]

# Data for the fifth line graph
x_values5 = [2019, 2020, 2021, 2022]
y_values5 = [19.4, 17.3, 18.2, 21.4]

# Create five line graphs
plt.plot(x_values1, y_values1, marker='o', linestyle='--', color='blue', label='under 20')
plt.plot(x_values2, y_values2, marker='s', linestyle='--', color='green', label='30')
plt.plot(x_values3, y_values3, marker='o', linestyle='-', color='yellow', label='40')
plt.plot(x_values4, y_values4, marker='s', linestyle='--', color='orange', label='50')
plt.plot(x_values5, y_values5, marker='o', linestyle='-', color='black', label='over 60')

# Adding labels and title
plt.xlabel('Years')
plt.ylabel('Values(%)')
plt.title('Different ages, "have pet(s)"')

# Adding a legend
plt.legend()

# Display the line graphs
plt.show()


# In[50]:


# 4) 2019~2022 -> 주택형태(단독주택, 아파트, 다세대주택, 연립/기타) 단독주택 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "주택형태" AND
   string_field_1 = "단독주택"
"""


# In[51]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[52]:


# 4) 2019~2022 -> 주택형태(단독주택, 아파트, 다세대주택, 연립/기타) 아파트 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "주택형태" AND
   string_field_1 = "아파트"
"""


# In[53]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[54]:


# 4) 2019~2022 -> 주택형태(단독주택, 아파트, 다세대주택, 연립/기타) 다세대주택 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "주택형태" AND
   string_field_1 = "다세대주택"
"""


# In[55]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[56]:


# 4) 2019~2022 -> 주택형태(단독주택, 아파트, 다세대주택, 연립/기타) 연립/기타 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "주택형태" AND
   string_field_1 = "연립/기타"
"""


# In[57]:


df = client.query(sql).to_dataframe()
df


# In[63]:


# 4) 2019~2022 -> 주택형태(단독주택, 아파트, 다세대주택, 연립/기타) 단독주택 -> 반려동물 유무 -> 있다
# 4) 2019~2022 -> 주택형태(단독주택, 아파트, 다세대주택, 연립/기타) 아파트 -> 반려동물 유무 -> 있다
# 4) 2019~2022 -> 주택형태(단독주택, 아파트, 다세대주택, 연립/기타) 다세대주택 -> 반려동물 유무 -> 있다
# 4) 2019~2022 -> 주택형태(단독주택, 아파트, 다세대주택, 연립/기타) 연립/기타 -> 반려동물 유무 -> 있다
# 그래프 합치기

import matplotlib.pyplot as plt

# Data for the first line graph
x_values1 = [2019, 2020, 2021, 2022]
y_values1 = [20.7, 19.7, 19.1, 19.5]

# Data for the second line graph
x_values2 = [2019, 2020, 2021, 2022]
y_values2 = [22.2, 20.7, 20.9, 25.5]

# Data for the third line graph
x_values3 = [2019, 2020, 2021, 2022]
y_values3 = [17.2, 19.3, 18.0, 20.5]

# Data for the fourth line graph
x_values4 = [2019, 2020, 2021, 2022]
y_values4 = [16.0, 19.3, 18.5, 19.1]

# font_path = 

# Create four line graphs
plt.plot(x_values1, y_values1, marker='o', linestyle='-', color='blue', label='detached')
plt.plot(x_values2, y_values2, marker='s', linestyle='--', color='green', label='apartment')
plt.plot(x_values3, y_values3, marker='o', linestyle='-', color='yellow', label='multiplex')
plt.plot(x_values4, y_values4, marker='s', linestyle='--', color='orange', label='others')

# Adding labels and title
plt.xlabel('Years')
plt.ylabel('Values(%)')
plt.title('Different house types, "have pet(s)"')

# Adding a legend
plt.legend()

# Display the line graphs
plt.show()


# In[64]:


# 5) 2019~2022 -> 가구원수(1인, 2인, 3인, 4인, 5인 이상) 1인 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "가구원수" AND
   string_field_1 = "1인"
"""


# In[65]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[66]:


# 5) 2019~2022 -> 가구원수(1인, 2인, 3인, 4인, 5인 이상) 2인 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "가구원수" AND
   string_field_1 = "2인"
"""


# In[67]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[74]:


# 5) 2019~2022 -> 가구원수(1인, 2인, 3인, 4인, 5인 이상) 3인 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "가구원수" AND
   string_field_1 = "3인"
"""


# In[75]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[76]:


# 5) 2019~2022 -> 가구원수(1인, 2인, 3인, 4인, 5인 이상) 4인 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "가구원수" AND
   string_field_1 = "4인"
"""


# In[77]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[82]:


# 5) 2019~2022 -> 가구원수(1인, 2인, 3인, 4인, 5인이상) 5인이상 -> 반려동물 유무 -> 있다

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_2,
   string_field_10,
   string_field_19,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "가구원수" AND
   string_field_1 = "5인이상"
"""


# In[83]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[85]:


# 5) 2019~2022 -> 가구원수(1인, 2인, 3인, 4인, 5인 이상) 1인 -> 반려동물 유무 -> 있다
# 5) 2019~2022 -> 가구원수(1인, 2인, 3인, 4인, 5인 이상) 2인 -> 반려동물 유무 -> 있다
# 5) 2019~2022 -> 가구원수(1인, 2인, 3인, 4인, 5인 이상) 3인 -> 반려동물 유무 -> 있다
# 5) 2019~2022 -> 가구원수(1인, 2인, 3인, 4인, 5인 이상) 4인 -> 반려동물 유무 -> 있다
# 5) 2019~2022 -> 가구원수(1인, 2인, 3인, 4인, 5인이상) 5인이상 -> 반려동물 유무 -> 있다
# 그래프 합치기

import matplotlib.pyplot as plt

# Data for the first line graph
x_values1 = [2019, 2020, 2021, 2022]
y_values1 = [19.9, 15.5, 14.7, 18.2]

# Data for the second line graph
x_values2 = [2019, 2020, 2021, 2022]
y_values2 = [22.3, 20.7, 21.3, 25.3]

# Data for the third line graph
x_values3 = [2019, 2020, 2021, 2022]
y_values3 = [19.7, 21.4, 21.9, 25.4]

# Data for the fourth line graph
x_values4 = [2019, 2020, 2021, 2022]
y_values4 = [18.0, 23.2, 23.3, 22.8]

# Data for the fifth line graph
x_values5 = [2019, 2020, 2021, 2022]
y_values5 = [19.7, 31.5, 26.6, 20.8]

# Create five line graphs
plt.plot(x_values1, y_values1, marker='o', linestyle='--', color='blue', label='single')
plt.plot(x_values2, y_values2, marker='s', linestyle='--', color='green', label='2 person')
plt.plot(x_values3, y_values3, marker='o', linestyle='-', color='yellow', label='3 person')
plt.plot(x_values4, y_values4, marker='s', linestyle='--', color='orange', label='4 person')
plt.plot(x_values5, y_values5, marker='o', linestyle='-', color='black', label='over 5 person')

# Adding labels and title
plt.xlabel('Years')
plt.ylabel('Values(%)')
plt.title('Different household members, "have pet(s)"')

# Adding a legend
plt.legend()

# Display the line graphs
plt.show()


# In[87]:


# 6) 2019~2022 -> 서울시 반려동물 입양 경로(동물판매업소(애견판매업소 동물병원 등)

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_4,
   string_field_12,
   string_field_21,
   string_field_30
FROM 
   project1.pets
WHERE
   string_field_0 = "서울시" AND
   string_field_1 = "소계"
"""


# In[88]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[89]:


# 6) 2019~2022 -> 서울시 반려동물 입양 경로(친지 친구 등 아는 사람을 통해 유상 입양)

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_5,
   string_field_13,
   string_field_22,
   string_field_31
FROM 
   project1.pets
WHERE
   string_field_0 = "서울시" AND
   string_field_1 = "소계"
"""


# In[90]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[91]:


# 6) 2019~2022 -> 서울시 반려동물 입양 경로(친지 친구 등 아는 사람을 통해 무상 입양)

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_6,
   string_field_14,
   string_field_23,
   string_field_32
FROM 
   project1.pets
WHERE
   string_field_0 = "서울시" AND
   string_field_1 = "소계"
"""


# In[92]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[93]:


# 6) 2019~2022 -> 서울시 반려동물 입양 경로(인터넷을 통해 구입)

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_7,
   string_field_15,
   string_field_24,
   string_field_33
FROM 
   project1.pets
WHERE
   string_field_0 = "서울시" AND
   string_field_1 = "소계"
"""


# In[94]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[95]:


# 6) 2019~2022 -> 서울시 반려동물 입양 경로(유기동물 입양)

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_8,
   string_field_16,
   string_field_25,
   string_field_34
FROM 
   project1.pets
WHERE
   string_field_0 = "서울시" AND
   string_field_1 = "소계"
"""


# In[96]:


df = client.query(sql).to_dataframe()
df


# In[ ]:





# In[97]:


# 6) 2019~2022 -> 서울시 반려동물 입양 경로(원래 기르던 동물이 낳은 새끼)

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_9,
   string_field_17,
   string_field_26,
   string_field_35
FROM 
   project1.pets
WHERE
   string_field_0 = "서울시" AND
   string_field_1 = "소계"
"""


# In[98]:


df = client.query(sql).to_dataframe()
df


# In[114]:


# 6) 2019~2022 -> 서울시 반려동물 입양 경로(동물판매업소(애견판매업소 동물병원 등)
# 6) 2019~2022 -> 서울시 반려동물 입양 경로(친지 친구 등 아는 사람을 통해 유상 입양)
# 6) 2019~2022 -> 서울시 반려동물 입양 경로(친지 친구 등 아는 사람을 통해 무상 입양)
# 6) 2019~2022 -> 서울시 반려동물 입양 경로(인터넷을 통해 구입)
# 6) 2019~2022 -> 서울시 반려동물 입양 경로(유기동물 입양)
# 6) 2019~2022 -> 서울시 반려동물 입양 경로(원래 기르던 동물이 낳은 새끼)
# 그래프 합치기

import matplotlib.pyplot as plt

# Data for the first line graph
x_values1 = [2019, 2020, 2021, 2022]
y_values1 = [25.1, 23.7, 25.7, 22.9]

# Data for the second line graph
x_values2 = [2019, 2020, 2021, 2022]
y_values2 = [17.3, 16.7, 17.1, 19.8]

# Data for the third line graph
x_values3 = [2019, 2020, 2021, 2022]
y_values3 = [35.7, 37.6, 37.5, 35.5]

# Data for the fourth line graph
x_values4 = [2019, 2020, 2021, 2022]
y_values4 = [4.4, 3.6, 2.3, 2.2]

# Data for the fifth line graph
x_values5 = [2019, 2020, 2021, 2022]
y_values5 = [11.6, 14.0, 14.2, 12.9]

# Data for the sixth line graph
x_values6 = [2019, 2020, 2021, 2022]
y_values6 = [5.9, 4.3, 3.2, 6.8]

# Create six line graphs
plt.plot(x_values1, y_values1, marker='o', linestyle='-', color='blue', label='animal store')
plt.plot(x_values2, y_values2, marker='s', linestyle='--', color='green', label='paid adoption')
plt.plot(x_values3, y_values3, marker='s', linestyle='--', color='yellow', label='free adoption')
plt.plot(x_values4, y_values4, marker='o', linestyle='-', color='orange', label='internet')
plt.plot(x_values5, y_values5, marker='o', linestyle='-', color='black', label='abandoned animal')
plt.plot(x_values6, y_values6, marker='s', linestyle='--', color='red', label='baby born')

# Adding labels and title
plt.xlabel('Years')
plt.ylabel('Values(%)')
plt.title('Pet Adoption Path')

# Adding a legend
plt.legend()

# Display the line graphs
plt.show()


# In[116]:


# 2019

import matplotlib.pyplot as plt

# Sample data
labels = ['Animal store', 'Paid adoption', 'Free adoption', 'Internet', 'Abandoned animal', 'Baby born']
sizes = [25.1, 17.3, 35.7, 4.4, 11.6, 5.9]

# Plot the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Add a title
plt.title('2019 Pet Adoption Path')

# Display the pie chart
plt.show()


# In[117]:


# 2020

import matplotlib.pyplot as plt

# Sample data
labels = ['Animal store', 'Paid adoption', 'Free adoption', 'Internet', 'Abandoned animal', 'Baby born']
sizes = [23.7, 16.7, 37.6, 3.6, 14.0, 4.3]

# Plot the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Add a title
plt.title('2020 Pet Adoption Path')

# Display the pie chart
plt.show()


# In[118]:


# 2021

import matplotlib.pyplot as plt

# Sample data
labels = ['Animal store', 'Paid adoption', 'Free adoption', 'Internet', 'Abandoned animal', 'Baby born']
sizes = [25.7, 17.1, 37.5, 2.3, 14.2, 3.2]

# Plot the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Add a title
plt.title('2021 Pet Adoption Path')

# Display the pie chart
plt.show()


# In[119]:


# 2022

import matplotlib.pyplot as plt

# Sample data
labels = ['Animal store', 'Paid adoption', 'Free adoption', 'Internet', 'Abandoned animal', 'Baby born']
sizes = [22.9, 19.8, 35.5, 2.2, 12.9, 6.8]

# Plot the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Add a title
plt.title('2022 Pet Adoption Path')

# Display the pie chart
plt.show()


# In[5]:


# 2020
# 소득과 반려동물 입양의 상관관계
# 100만원 미만

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_10
FROM 
   project1.pets
WHERE
   string_field_0 = "소득" AND
   string_field_1 = "100만원 미만"
"""


# In[6]:


df = client.query(sql).to_dataframe()
df


# In[7]:


# 2020
# 소득과 반려동물 입양의 상관관계
# 100-200만원 미만

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_10
FROM 
   project1.pets
WHERE
   string_field_0 = "소득" AND
   string_field_1 = "100-200만원 미만"
"""


# In[8]:


df = client.query(sql).to_dataframe()
df


# In[9]:


# 2020
# 소득과 반려동물 입양의 상관관계
# 200-300만원 미만

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_10
FROM 
   project1.pets
WHERE
   string_field_0 = "소득" AND
   string_field_1 = "200-300만원 미만"
"""


# In[10]:


df = client.query(sql).to_dataframe()
df


# In[11]:


# 2020
# 소득과 반려동물 입양의 상관관계
# 300-400만원 미만

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_10
FROM 
   project1.pets
WHERE
   string_field_0 = "소득" AND
   string_field_1 = "300-400만원 미만"
"""


# In[12]:


df = client.query(sql).to_dataframe()
df


# In[13]:


# 2020
# 소득과 반려동물 입양의 상관관계
# 400-500만원 미만

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_10
FROM 
   project1.pets
WHERE
   string_field_0 = "소득" AND
   string_field_1 = "400-500만원 미만"
"""


# In[14]:


df = client.query(sql).to_dataframe()
df


# In[15]:


# 2020
# 소득과 반려동물 입양의 상관관계
# 500만원 이상
sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_10
FROM 
   project1.pets
WHERE
   string_field_0 = "소득" AND
   string_field_1 = "500만원 이상"
"""


# In[16]:


df = client.query(sql).to_dataframe()
df


# In[34]:


# 2020 그래프

import matplotlib.pyplot as plt

# Sample data
x = ["under 100", "under 100-200", "under 200-300", "under 300-400", "under 400-500", "over 500"]
y = [12.0, 15.5, 17.9, 20.6, 21.2, 24.4]

# Rotate x-axis labels by 45 degrees
plt.xticks(rotation=45)

# Create a line graph
plt.plot(x, y, label='"have pet(s)"')

# Add labels and title
plt.xlabel('Earnings')
plt.ylabel('Values(%)')
plt.title('2020 Earnings and "have pet(s)"')

# Add a legend
plt.legend()

# Show the plot
plt.show()


# In[23]:


# 2022
# 소득과 반려동물 입양의 상관관계
# 200만원 미만

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "소득" AND
   string_field_1 = "200만원 미만"
"""


# In[24]:


df = client.query(sql).to_dataframe()
df


# In[25]:


# 2022
# 소득과 반려동물 입양의 상관관계
# 200-400만원 미만

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "소득" AND
   string_field_1 = "200-400만원 미만"
"""


# In[26]:


df = client.query(sql).to_dataframe()
df


# In[27]:


# 2022
# 소득과 반려동물 입양의 상관관계
# 400-600만원 미만

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "소득" AND
   string_field_1 = "400-600만원 미만"
"""


# In[28]:


df = client.query(sql).to_dataframe()
df


# In[29]:


# 2022
# 소득과 반려동물 입양의 상관관계
# 600-800만원 미만

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "소득" AND
   string_field_1 = "600-800만원 미만"
"""


# In[30]:


df = client.query(sql).to_dataframe()
df


# In[31]:


# 2022
# 소득과 반려동물 입양의 상관관계
# 800만원 이상

sql = """
SELECT  
   string_field_0,
   string_field_1,
   string_field_28
FROM 
   project1.pets
WHERE
   string_field_0 = "소득" AND
   string_field_1 = "800만원 이상"
"""


# In[32]:


df = client.query(sql).to_dataframe()
df


# In[35]:


# 2022 그래프

import matplotlib.pyplot as plt

# Sample data
x = ["under 200", "under 200-400", "under 400-600", "under 600-800", "over 800"]
y = [14.1, 19.9, 23.1, 26.5, 38.1]

# Rotate x-axis labels by 45 degrees
plt.xticks(rotation=45)

# Create a line graph
plt.plot(x, y, label='"have pet(s)"')

# Add labels and title
plt.xlabel('Earnings')
plt.ylabel('Values(%)')
plt.title('2022 Earnings and "have pet(s)"')

# Add a legend
plt.legend()

# Show the plot
plt.show()


# In[ ]:




