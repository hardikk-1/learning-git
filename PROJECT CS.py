#to edit records
def edit_details_voters():
    get_voterlist()
    name=input("\nenter voter's name:")
    attr=input("Enter attribute whose record needs to be edited: ")
    if attr.lower()=='registeration date':
        attr='Voter_Registeration_Date'
    elif attr.lower()=='name':
        attr='Voter_Name'
    elif attr.lower()=='dob':
        attr='Date_of_Birth'
    elif attr.lower()=='status':
        attr='Voter_Status'
    data=input("Enter updated data: ")
    sq1="Update eligiblevoters SET {}=%s WHERE voter_name=%s".format(attr)
    cur.execute(sq1,(data,name))
    con.commit()
    print("\nUPDATED")

#to get record
def get_voter():
    name=input("enter voter's name:")
    sq1="select * from eligiblevoters where voter_name=%s"
    cur.execute(sq1,(name,))
    data=cur.fetchall()
    table=tabulate(data,headers=['NAMER','GENDER','DOB','ADDRESS','STATUS','WARD','REGISTERATION DATE'],tablefmt='grid')
    print(table)

#To show voter's list
def get_voterlist():
    cur.execute("select * from eligiblevoters")
    data=cur.fetchall()
    table=tabulate(data,headers=['NAMER','GENDER','DOB','ADDRESS','STATUS','WARD','REGISTERATION DATE'],tablefmt='grid')
    print(table)

#To delete record
def delete_voter():
    get_voterlist()
    name=("\nenter votername whose record is to be deleted: ")
    cur.execute("delete from eligiblevoters where voter_name=%s",(name,))
    con.commit()
    print("\nDELETED")

#To get voters of a ward
def get_voters_ward():
    name=input("Enter ward name: ")
    cur.execute("select * from eligiblevoters where ward=%s",(name,))
    data=cur.fetchall()
    table=tabulate(data,headers=['NAMER','GENDER','DOB','ADDRESS','STATUS','WARD','REGISTERATION DATE'],tablefmt='grid')
    print(table)

#To get no. of voters
def count_voters():
    cur.execute("select * from eligiblvoters")
    cur.fetchall()
    print("\nNO. OF VOTERS: ".cur.rowcount)

def count_voters_gen():
    n=input("Which gender do you wish to check for? (M - MALE, F - FEMALE)")
    cur.execute("select * from eligiblevoters where gender = %s",(n,))
    cur.fetchall()
    print("\nNO. OF VOTERS: ",cur.rowcount)

'''infrastructure'''

# to add record
def create_infrastructure_record():
    while True:
        Tp = input('Enter the type of infrastructure (School, Roads, Residence, Office Hubs, Parks, Shopping Complexes, Other): ')
        location = input("Enter the location: ")
        project_id = int(input("Enter the DEVELOPMENT PROJECT ID:
        start_date =input("Enter the start date (yyyy-mm-dd): ")
        end_date = input("Enter the scheduled/expected end date (yyyy-mm-dd): ")
        budget = float(input("Enter the allotted budget: "))
        description = input("Enter any necessary description: ")
        status input("Enter the status(Ongoing,Completed, Planned, Under Construction, Delayed, On Hold,Cancelled): ")
        sql = "INSERT INTO Infrastructure (Type, Location, Project_ID, Start Date, End_Date, Budget, Description, Status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        values = (Tp, location, project_id, start_date, end_date, budget, description, status)
        cur.execute(sql, values)
        con.commit()
        print("\nRECORD ADDED.")
    ch=input("do you wish to add more records? (y/n): ")
    if ch=='y':
        pass    
    else:
        break

# Function to update an existing infrastructure record
def update_infrastructure_record():
    view_cur_infra_projects()
    name=input("\nenter project ID whose data needs to be updated: ")
    attr=input("enter attribute whose data is to be updated: ")
    if attr.lower()=='project id':
        attr='Project_ID'
    elif attr.lower()=='start date':
        attr="Start_Date'
    elif attr.lower()=='end date':
        attr='End_Date'
    data=input("enter new data: ")
    sql = "UPDATE Infrastructure SET {} = %s WHERE Project_ID = %s".format(attr)
    cur.execute(sql, (data, name))
    con.commit()
    print("\nUPDATED.")

# to delete a project
def delete_infra_project():
    view_cur_infra_projects()
    project_name=input("enter name of the project whose record you wish to delete: ")
    sql = "DELETE FROM Infrastructure WHERE Type = %s"
    cur.execute(sql, (project_name,))
    con.commit()
    print("\nDELETED.")

# to view projects
def view_one_infra():
    name = input("Enter project ID whose data needs to be viewed:")
    cur.execute("select * from infrastructure where project_id = %s", (name,))
    data=cur.fetchall()
    table=tabulate(data, headers=['TYPE', 'LOCATION','PROJECT ID','START DATE','END DATE','BUDGET', 'DESCRIPTION','STATUS'], tablefmt='grid')
    print(table)

def view_cur_infra_projects():
    cur.execute("select * from infrastructure")
    data=cur.fetchall()
    table=tabulate(data, headers=['TYPE', 'LOCATION', 'PROJECT ID','START DATE', 'END DATE', 'BUDGET', 'DESCRIPTION', 'STATUS'],
    tablefmt='grid')
    print(table)

def get_infra():
    name = input("Enter type of project you want to search") cur.execute("select * from infrastructure where type = %s",(name,))
    data=cur.fetchall()
    table=tabulate(data, headers=['TYPE', 'LOCATION', 'PROJECT ID','START DATE','END DATE', 'BUDGET', 'DESCRIPTION', 'STATUS'], tablefmt='grid')
    print(table)

def get_one_budg_infra():
    name = input("Enter type of infrastructure whose budget you wish to combine: ")
    cur.execute("select sum(budget) from infrastructure where type=%s", (name,))
    data=cur.fetchall()
    for i in data:
        print (i)

'''cooperatives-shgs'''

#to add a record
def create_cooperative_or_shg():
    while True:
        group_name = input("enter group name: ")
        formation_date = input("enter the formation date: ")
        location = input("enter the location: ")
        total_members = int(input("enter the number of members:"))
        activities = input("describe the activities of the group: ") financial_data = int(input("enter the financial data of the group "))
        contact_information = input("enter the contact information of group members: """)
        sql = "INSERT INTO Cooperatives_SHGS (Group_Name, Formation_Date,
        Location, Total_Members, Activities, Financial_Data, Contact_Information) VALUES (%s, %s, %s, %s, %s, %, %s) values = (group_name, formation_date, location, total_members, activities,
        financial_data, contact_information)
        cur.execute(sql, values)
        con.commit()
        print("\nRECORD ADDED")
        ch=input("do you wish to add more records? (y/n) ")
        if ch=='y':
            pass
        else:
            break

# Function to update an existing cooperative or SHG record
def update_cooperative_or_shg():
    view_cooperatives_and_shgs()
    name=input("enter group name whose data needs to be updated: ")
    attr= input("enter attribute whose data is to be updated: ")
    if attr.lower()=='group name':
        attr='Group_Name'
    if attr.lower()=='formation date':
        attr='Formation_Date'
    if attr.lower()=='total members':
        attr='Total_Members'
    if attr.lower()=='financial data':
        attr='FINANCIAL_DATA'
    if attr.lower()=='contact information':
        attr='Contact_Information'
    data=input("enter new data: ")
    sql = "UPDATE Cooperatives_SHGS SET {} = %s WHERE Group_name=%s".format(attr)
    cur.execute(sql, (data, name))
    con.commit()
    print("\nUPDATED.")

# Function to delete a cooperative or SHG record
def delete_cooperative_or_shg():
    view_cooperatives_and_shgs()
    group_name=input("\nenter name of the group whose record you wish to delete: ")
    sql = "DELETE FROM Cooperatives_SHGS WHERE Group_name = %s"
    cur.execute(sql, (group_name,))
    con.commit()
    print("\nDELETED.")

#To view records in the Cooperatives and SHG's table
def view_cooperatives_and_shgs():
    sql = "UPDATE Cooperatives_SHGS SET {} = %s WHERE Group_name=%s".format(attr)
    cur.execute(sql, (data, name))
    con.commit()
    print("\nUPDATED.")

# Function to delete a cooperative or SHG record
def delete_cooperative_or_shg():
    view_cooperatives_and_shgs()
    group_name=input("\nenter name of the group whose record you wish to delete: ")
    sql = "DELETE FROM Cooperatives_SHGS WHERE Group_name = %s"
    cur.execute(sql, (group_name,))
    con.commit()
    print("\nDELETED.")

#To view records in the Cooperatives and SHG's table
def view_cooperatives_and_shgs():
    sql = "SELECT * FROM Cooperatives_SHGs"
    cur.execute(sql)
    data = cur.fetchall()
    table=tabulate(data, headers=['GROUP NAME', 'FORMATION DATE', 'LOCATION', 'TOTAL MEMBERS', 'ACTIVITIES', 'FINANCIAL DATA','CONTACT INFO'], tablefmt='grid')
    print(table)

def view_one_coop_or_shg():
    name = input("Enter group name whose data needs to be viewed: ")
    cur.execute("select * from cooperatives_shgs where group_name=%s", (name,))
    data=cur.fetchall()
    table=tabulate(data, headers=['GROUP NAME','FORMATION DATE', 'LOCATION', 'TOTAL MEMBERS', 'ACTIVITIES', 'FINANCIAL DATA','CONTACT INFO'], tablefmt='grid')
    print(table)

def get_num_coop_or_shg():
    cur.execute("select * from cooperatives_shgs")
    cur.fetchall()
    print("\nNO. OF GROUPS IN THIS VILLAGE: ", cur.rowcount)

'''government initiatives'''

#add record
def create_governance_initiative():
    while True:
        initiative_name = input("enter initiative name: ")
        initiative_type = input("enter initiative type(Medicaid, Housing, Senior Citizens, Education, Agricultural, Other): ") description = input("enter a suitable description: ") start_date = input("enter the start date(yyyy-mm-dd): ")
        budget = float(input("enter the allotted budget: "))
        key_stakeholders = input("enter the details of key parties involved: ")
        progress_updates = input("enter any progress updates: ")
        sql = "INSERT INTO Governance (Initiative_Name, initiative_type, description, Start_Date, Budget,Key_Stakeholders, Progress_Updates) VALUES (%s, %, %, %, %s, %s, %s)"
        values=(initiative_name, initiative_type, description, start_date, budget, key_stakeholders, progress_updates)
        cur.execute(sql, values)
        con.commit()
        print("\nRECORD ADDAED.")
        ch=input("do you wish to add more records? (y/n) ")
        if ch=='y':
            pass
        else:
            break

#Function to update an existing governance initiative record
def update_governance_initiative():
    view_governance_initiatives()
    name=input("\nenter initiative name whose data needs to be updated: ")
    attr= input("enter attribute whose data is to be updated: ")
    if attr.lower()=='initiative name':
        attr='Initiative_Name'
    if attr.lower()=='initiative type':
        attr='Initiative_type'
    if attr.lower()=='start date':
        attr='Start Date'
    if attr.lower()=='key stakeholders':
        attr='Key_Stakeholders'
    if attr.lower()=='progress updates':
        attr='Progress_Updates'
    data=input("enter new data: ")
    sql = "UPDATE Governance SET {} = %s WHERE Initiative_name =%s".format(attr)
    cur.execute(sql, (data, name))
    con.commit()
    print("\nUPDATED.")

#Function to delete a governance initiative record
def delete_governance_initiative():
    initiative_name=input("\nenter name of the initiative whose record you wish to delete: ")
    sql = "DELETE FROM Governance WHERE Initiative_name=%s"
    cur.execute(sql, (initiative_name,))
    con.commit()
    print("\nDELETED.")

# Function to view all records in the Governance table
def view_governance_initiatives():
    sql = "SELECT * FROM Governance"
    cur.execute(sql)
    data = cur.fetchall()
    table=tabulate(data, headers=['INITIATIVE NAME','INITIATIVE TYPE','DESCRIPTION', 'START DATE', 'BUDGET','KEY STAKEHOLDERS','PROGRESS UPDATES'], tablefmt='grid')
    print(table)

def view_one_govt_init():
    name = input("Enter initiative whose data needs to be viewed:
    cur.execute("select * from governance where initiative_name=%s", (name,))
    data=cur.fetchall()
    table=tabulate(data, headers=['INITIATIVE NAME', 'INITIATIVE TYPE', 'DESCRIPTION', 'START DATE', 'BUDGET', 'KEY STAKEHOLDERS', 'PROGRESS UPDATES'], tablefmt='grid')
    print(table)

def view_type_govt_init():
    name = input("Enter type of initiative whose data needs to be viewed: ")
    cur.execute("select * from governance where initiative_type => %s", (name,))
    data=cur.fetchall()
    table=tabulate(data, headers=['INITIATIVE NAME', 'INITIATIVE TYPE', 'DESCRIPTION','START DATE', 'BUDGET', 'KEY STAKEHOLDERS', 'PROGRESS UPDATES'], tablefmt='grid')
    print(table)

def get_comb_budg_govt_init():
    cur.execute("select sum(budget) from governance")
    data=cur.fetchall()
    for i in data:
        print (i)

def get_one_budg_govt_init():
    name = input("Enter type of initiative whose budget you wish to combine: ")
    cur.execute("select sum(budget) from governance where initiative_type = %s", (name,))
    data=cur.fetchall()
    for i in data:
        print (i)    





























        

    





    
