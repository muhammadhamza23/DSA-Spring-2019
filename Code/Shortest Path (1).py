G={}

source=input('Enter Your Location: ')
destination=input('Enter Your Destination: ')

import turtle

background=turtle.Screen()

# Coordinates dictionary is for lower ground and 2nd floor turtle GUI.
Coordinates={
    'E-017':['Dukan',(-360,-23)],
   'E-013':['Tapal Cafeteria',(-360,-37)],
   'E-012':['Rangoonwala Classroom',(-268,-72)],
   'E-011':['Dinshaw Seminar Room',(-262,-72)],
   'E-010':['Visualization & Graphic Lab',(-250,-72)],
   'E-003':['Linux & Networking Lab',(-200,-67)],
   'E-002':['Media Mouck-up Studio',(-200,-60)],
   'C-025':['Engineering Workshop',(-294,60)],
   'C-023':['Head of Administration and Campus Services',(-400,20)],
   'C-022':['Administration and Safety Offices',(-400,45)],
   'C-018':['Female Gym',(-430,12)],
   'C-017':['Co-Ed Gym',(-430,12)],
   'C-015':['Classroom',(-400,-9)],
   'C-007':['Project Lab',(-277,-37)],
   'C-004':['Power Lab',(-245,-37)],
   'C-001':['Circuits & Electronics Lab',(-200,-37)],
   'W-007':['Plantroom',(-335,95)],
   'W-004':['Facilities Offices',(-280,60)],
   'LB-001':['EHSAS',(-120,-60)],
   '001':['LEARN',(-175,37)],
   '002':['Indoor Games',(-400,12)],
   '003':['Fries',(-400,-22)],
   '004':['Junction',(-290,-65)],
   '005':['EE Labs',(-172,-33)],
   '006':['Sports Court',(-510,-22)],
   '007':['Dhaba',(-400,-50)],
   '008':['Exit',(-315,-75)],
   '009':['Washroom01',(-360,-8)],
   '010':['Washroom02',(-210,-67)],
   '011':['Pool',(-400,60)],
   '012':['Lift01',(-255,60)],

    '128':['Lift11',(-250,70)],
    '214':['Lift21',(-250,70)],

    'W-300':['Faculty Pod',(-350,70)],
   'W-311':['Projects Lab',(-250,35)],
   '302':['Lift31',(-250,70)]
    }


N={'E-017':'Dukan',
   'E-013':'Tapal Cafeteria',
   'E-012':'Rangoonwala Classroom',
   'E-011':'Dinshaw Seminar Room',
   'E-010':'Visualization & Graphic Lab',
   'E-003':'Linux & Networking Lab',
   'E-002':'Media Mouck-up Studio',
   'C-025':'Engineering Workshop',
   'C-023':'Head of Administration and Campus Services',
   'C-022':'Administration and Safety Offices',
   'C-018':'Female Gym',
   'C-017':'Co-Ed Gym',
   'C-015':'Classroom',
   'C-007':'Project Lab',
   'C-004':'Power Lab',
   'C-001':'Circuits & Electronics Lab',
   'W-007':'Plantroom',
   'W-004':'Facilities Offices',
   'LB-001':'EHSAS',
   '001':'LEARN',
   '002':'Indoor Games',
   '003':'Fries',
   '004':'Junction',
   '005':'EE Labs',
   '006':'Sports Court',
   '007':'Dhaba',
   '008':'Exit',
   '009':'Washroom01',
   '010':'Washroom02',
   '011':'Pool',
   '012':'Lift01',

   'E-121':'Soorty Lecture Theater',
   'E-105':'Faculty Pod',
   'E-101':'Cassim Computing Lab',
   'E-100':'Agha Multipurpose Hall',
   'C-110':'Student Lounge',
   'C-110A':'Student lounge second entrance',
   'C-109':'Arif Habib Classroom',
   'C-114':'Faculty Pod',
   'C-100':'Faculty Pod',
   'W-114':'Dig. Sys. & Instrumentation',
   'W-111':'Communication Lab',
   'W-110':'G.M. Adamjee Math Lab',
   'W-121':'Ecology Lab',
   'W-118':'Chemistry Lab',
   'W-100':'Physics Lab',
   'LB-100':'Library & Information Commons',
   'SC-100':'Student Center',
   '106':'Entrance',
   '107':'CS1',
   '108':'CS2',
   '109':'CS3',
   '110':'CS4',
   '111':'CS5',
   '112':'CS6',
   '113':'CS7',
   '114':'CS8',
   '115':'CS9',
   '116':'Water Courtyard',
   '117':'Corn',
   '118':'Library Door',
   '119':'Cafe2Go',
   '120':'Info Commons',
   '121':'HS & SL',
   '122':'R1',
   '123':'R2',
   '124':'R3',
   '125':'DSA',
   '126':'ATM',
   '127':'Courts',
   '128':'Lift11',
   '129':'Bank',
   '130':'Health Services',
   '131':'Student Life',
   '132':'Writing Center',
   '133':'Reception',
   '134':'Lift12',
   '135':'Lift13',
   '136':'Washroom11',
   '137':'Washroom12',
   '138':'Washroom13',
   '139':'Washroom14',
   '140':'Up1',
   '141':'Down1',

   'N-200':'Faculty Pod',
   'N-219':'Gulamali Habib Classroom',
   'N-220':'Standard Chartered Classroom',
   'E-220':'Tariq Rafi Lecture Theater',
   'E-226':'Film Studio',
   'E-215':'Auditorium',
   'C-203':'Faculty Pod',
   'C-201':'Center for Pedagogical Excellence',
   'C-200':'Kassim Parekh Classroom',
   'W-244':'Design Studio',
   'W-243':'Classroom',
   'W-242':'Javat Seminar Room',
   'W-221':'Faculty Pod',
   'W-234':'Mahmood Nensey Classroom',
   'LB-200':'Library & Information Commons',
   '201':'To Baithak',
   '202':'To Faculty',
   '203':'slope 2',
   '204':'Corridor 1',
   '205':'Corridor 2',
   '206':'Auditorium Stage',
   '207':'Library Reception',
   '208':'stairs1',
   '209':'Tables',
   '210':'Washroom21',
   '211':'Washroom22',
   '212':'Washroom23',
   '213':'Yohsin',
   '214':'Lift21',
   '215':'Lift22',
   '216':'Lift23',
   '217':'Baithak',
   '218':'stairs2',
   '219':'Up2',
   '220':'Down2',

   'W-300':'Faculty Pod',
   'W-311':'Projects Lab',
   '302':'Lift31',

   'N-408':'Prayer Room (Female)',
   'N-407':'Prayer Room (Male)',
   'N-400':'Staff Dining Hall',
   '401':'Lift42',
   '402':'Child-Care Center'
   }


E=[('005', '109', 35, 'Open'),
       ('005', 'C-001', 16, 'Open'),
       ('005', '001', 48, 'Open'),
       ('001', '141', 30, 'Open'),
       ('001', '012', 62, 'Open'),
       ('012', 'W-004', 15, 'Open'),
       ('W-004', 'C-025', 6, 'Open'),
       ('C-025', '011', 57, 'Open'),
       ('011', 'C-022', 8.5, 'Open'),
       ('C-022', 'C-023', 13, 'Open'),
       ('C-023', '002', 4, 'Open'),
       ('002', 'C-018', 17, 'Open'),
       ('002', 'C-017', 17, 'Open'),
       ('002', 'C-015', 12, 'Open'),
       ('C-015', '009', 26, 'Open'),
       ('C-015', '003', 25, 'Open'),
       ('009', 'E-017', 19, 'Open'),
       ('E-017', '003', 21, 'Open'),
       ('003', '006', 65, 'Open'),
       ('003', '007', 21, 'Open'),
       ('E-017', 'E-013', 8, 'Open'),
       ('E-013', 'C-007', 44, 'Open'),
       ('C-007', '004', 26, 'Open'),
       ('C-007', 'C-004', 21, 'Open'),
       ('C-004', 'C-001', 21, 'Open'),
       ('C-001', 'E-002', 13, 'Open'),
       ('E-002', 'E-003', 4, 'Open'),
       ('E-002', '010', 4, 'Open'),
       ('E-003', 'E-010', 33, 'Open'),
       ('010', 'E-010', 33, 'Open'),
       ('E-010', 'E-011', 4, 'Open'),
       ('E-011', 'E-012', 4, 'Open'),
       ('E-012', '008', 10, 'Open'),
       ('E-012', '004', 11, 'Open'),
       ('008', '004', 9, 'Open'),
       ('008', 'E-226', 100, 'Open'),
       ('004', 'E-105', 105, 'Open'),
       ('124', '127', 205, 'Open'),
       ('124', '123', 31, 'Open'),
       ('124', '116', 31, 'Open'),
       ('123', '122', 25, 'Open'),
       ('123', '128', 14, 'Open'),
       ('123', 'W-100', 14, 'Open'),
       ('123', 'W-110', 14, 'Open'),
       ('122', '121', 41, 'Open'),
       ('122', '129', 75, 'Open'),
       ('129', '106', 58, 'Open'),
       ('W-114', '116', 79, 'Open'),
       ('W-114', 'C-110A', 57, 'Open'),
       ('W-111', '116', 79, 'Open'),
       ('W-111', 'C-110A', 57, 'Open'),
       ('W-121', '116', 79, 'Open'),
       ('W-121', 'C-110A', 57, 'Open'),
       ('W-118', '116', 79, 'Open'),
       ('W-118', 'C-110A', 57, 'Open'),
       ('116', '117', 16, 'Open'),
       ('116', 'W-100', 26, 'Open'),
       ('116', 'W-110', 26, 'Open'),
       ('116', '128', 26, 'Open'),
       ('128', '140', 7, 'Open'),
       ('128', '138', 8, 'Open'),
       ('128', '214', 0, 'Open'),
       ('128', '012', 0, 'Open'),
       ('W-100', '141', 7, 'Open'),
       ('W-100', '138', 8, 'Open'),
       ('W-110', '140', 7, 'Open'),
       ('W-110', '138', 8, 'Open'),
       ('130', '121', 24, 'Open'),
       ('121', '131', 11, 'Open'),
       ('140', '141', 4, 'Open'),
       ('140', 'W-100', 7, 'Open'),
       ('140', 'W-110', 7, 'Open'),
       ('140', '128', 7, 'Open'),
       ('141', '117', 20, 'Open'),
       ('117', '141', 16, 'Open'),
       ('117', 'C-109', 6, 'Open'),
       ('C-109', '117', 6, 'Open'),
       ('134', 'SC-100', 17, 'Open'),
       ('134', '108', 26, 'Open'),
       ('134', '215', 0, 'Open'),
       ('C-110A', 'C-015', 33, 'Open'),
       ('C-110A', '114', 17, 'Open'),
       ('SC-100', '136', 14, 'Open'),
       ('127', '115', 43, 'Open'),
       ('115', 'C-114', 11, 'Open'),
       ('115', 'C-110', 17, 'Open'),
       ('115', '003', 50, 'Open'),
       ('C-110', '139', 14, 'Open'),
       ('139', 'C-110', 14, 'Open'),
       ('114', 'C-110', 10, 'Open'),
       ('114', '113', 22, 'Open'),
       ('113', 'E-121', 21, 'Open'),
       ('113', '126', 43, 'Open'),
       ('E-121', '114', 21, 'Open'),
       ('112', '126', 20, 'Open'),
       ('112', 'C-109', 26, 'Open'),
       ('112', '111', 11, 'Open'),
       ('111', 'C-100', 10, 'Open'),
       ('111', '110', 37, 'Open'),
       ('110', '131', 18, 'Open'),
       ('110', '118', 17, 'Open'),
       ('110', '109', 15, 'Open'),
       ('110', '136', 35, 'Close'),
       ('109', '005', 35, 'Open'),
       ('109', '133', 34, 'Open'),
       ('133', 'SC-100', 18, 'Open'),
       ('108', '133', 9, 'Open'),
       ('107', '108', 23, 'Open'),
       ('107', 'E-100', 20, 'Open'),
       ('107', '106', 23, 'Open'),
       ('120', 'LB-200', 50, 'Open'),
       ('120', '118', 14, 'Open'),
       ('120', '135', 28, 'Open'),
       ('120', '137', 18, 'Open'),
       ('132', '120', 31, 'Open'),
       ('119', '118', 13, 'Open'),
       ('125', '119', 20, 'Open'),
       ('125', 'E-101', 5, 'Open'),
       ('E-105', '125', 9, 'Open'),
       ('E-105', '004', 105, 'Open'),
       ('135', '132', 3, 'Open'),
       ('135', '216', 0, 'Open'),
       ('217', '201', 37, 'Open'),
       ('201', 'W-243', 8.5, 'Open'),
       ('W-243', 'W-244', 9, 'Open'),
       ('201', 'W-242', 8.5, 'Open'),
       ('W-242', '202', 21, 'Open'),
       ('202', '203', 29, 'Open'),
       ('202', '214', 22, 'Open'),
       ('203', '117', 100, 'Open'),
       ('203', '218', 19, 'Open'),
       ('218', '126', 43, 'Open'),
       ('218', 'E-220', 18, 'Open'),
       ('E-220', 'E-226', 30, 'Open'),
       ('E-226', '207', 62, 'Open'),
       ('207', '211', 15, 'Open'),
       ('207', '216', 15.5, 'Open'),
       ('216', '213', 10, 'Open'),
       ('207', 'LB-200', 19.5, 'Open'),
       ('LB-200', '209', 17, 'Open'),
       ('209', '206', 29, 'Open'),
       ('209', 'C-201', 10, 'Open'),
       ('C-200', '205', 10, 'Open'),
       ('204', 'C-203', 33, 'Open'),
       ('204', 'C-201', 9, 'Open'),
       ('C-203', '219', 3, 'Open'),
       ('219', '220', 4, 'Open'),
       ('220', '140', 40, 'Open'),
       ('220', '214', 12, 'Open'),
       ('214', '212', 10, 'Open'),
       ('214', 'W-234', 6, 'Open'),
       ('214', '302', 0, 'Open'),
       ('214', 'W-221', 4, 'Open'),
       ('204', '205', 25.5, 'Open'),
       ('205', 'N-200', 13, 'Open'),
       ('205', 'N-219', 13, 'Open'),
       ('205', 'N-220', 13, 'Open'),
       ('N-200', '210', 25.5, 'Open'),
       ('C-200', '206', 16, 'Open'),
       ('206', 'E-215', 19.5, 'Open'),
       ('E-215', '208', 17, 'Open'),
       ('C-200', '215', 8.5, 'Open'),
       ('208', '106', 75, 'Close'),
       ('215', '208', 8.5, 'Open'),
       ('215', '401', 0, 'Open'),
       ('W-311', '302', 11, 'Open'),
       ('302', 'W-300', 11, 'Open'),
       ('W-311', '219', 85, 'Open'),
       ('302', '219', 85, 'Open'),
       ('401', '402', 10, 'Open'),
       ('402', 'N-400', 17, 'Open'),
       ('402', 'N-408', 16, 'Open'),
       ('N-408', 'N-407', 7, 'Open')]
def addNodes(G,nodes):
    for i in nodes.keys():
        G[i]=[]
    return(G)
def addEdges(G,edges,directed=False):
    for i in edges:
        G[i[0]].append((i[1],i[2],i[3]))
        G[i[1]].append((i[0],i[2],i[3]))
    return(G)
def graph(G,N,E):
    G=addNodes(G,N)
    G=addEdges(G,E)
    return(G)

def dijkstra(G,source,destination):
    import math
    distances={}
    for node in G.keys():
        distances.update({node:float('inf')})
        distances.update({source:0})
    parents={}
    for node in G.keys():
        parents.update({node:None})
        parents.update({source:source})
   
    visited=[]
    un_visited=[a for a in G.keys()]
   
    while len(un_visited)!=0:
        min_distance=float('inf')
        current_node=''
        for node,distance in distances.items():
            if node!=destination and min_distance>distance and node not in visited:
                min_distance=distance
                current_node=node
        if current_node=='':
            break
        for neighbor in G[current_node]:
          if neighbor[2] == "Open":
              if distances[neighbor[0]]<=min_distance+int(neighbor[1]):
                pass
              else:
                distances[neighbor[0]]=min_distance+int(neighbor[1])
                parents[neighbor[0]]=current_node
                   
        visited.append(current_node)
        un_visited.remove(current_node)
    path=[]
    # This while loop will generate the shortest path.
    while source!=destination:
        parent=parents[destination]
        distance=distances[destination]
        path.append((parent,destination,distance))
        destination=parent
    return path[::-1]

shortest_path=(dijkstra(graph(G,N,E),source,destination))
print(shortest_path)
print('\n')
# Below are the directions being printed for the turtle GUI.
print('Student.goto'+str(Coordinates[shortest_path[0][0]][1]))
print('Student.showturtle()')
print('Student.pendown()')
for i in shortest_path:
    if i[1]=='W-300' or i[1]=='W-311' or i[1]=='302' or i[1]=='128' or i[1]=='214':
        print("background.bgpic('2nd Floor.gif')")
        print('Student.goto'+str(Coordinates[i[1]][1]))
    else:
        print('Student.goto'+str(Coordinates[i[1]][1]))
