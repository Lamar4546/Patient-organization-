'''Group Information
    DianaJohnson:620160843
    LamarShaw: 620164330'''

"""part 1"""

def makePatient(age,sex,trestbps,chol,fbs,thalach,oldpeak):
#Creates and returns a patient tuple with the structure ('HDPT', PatientDictionary).
#PatientDictionary is a dictionary containing patient information (age, sex, trestbps, chol, fbs, thalach, oldpeak).
    PatientDictionary= {'age':age,'sex':sex,'trestbps':trestbps,'chol':chol,'fbs':fbs,'thalach':thalach,'oldpeak':oldpeak}
    return ('HDPT',PatientDictionary)


def getPatientAge(pt):
#Returns the age in patient Dictionary
    return pt[1]['age']

def getPatientSex(pt):
#Returns the sex in patient Dictionary
    return pt[1]['sex']

def getPatientTres(pt):
#Returns the trestbps in patient Dictionary
    return pt[1]['trestbps']

def getPatientChol(pt):
#Returns the cholesterol in patient Dictionary
    return pt[1]['chol']

def getPatientFbs(pt):
#Returns the fbs in patient Dictionary
    return pt[1]['fbs']

def getPatientTlach(pt):
#Returns the thalach(heartrate) in patient Dictionary
    return pt[1]['thalach']

def getPatientST(pt):
#Returns the oldpeak in patient Dictionary
    return pt[1]['oldpeak']

def isPatient(pt):
#checks to see if the input is a valid paitent 
    return type(pt)==tuple and pt[0]=='HDPT' and type(pt[1])== dict

def isEmptyPt(pkt):
#checks to see if the given patient is empty
    return pkt[1]=={} or len(pkt[1])==0 or pkt=='HDPT' or pkt('HDPT',{})

def patientInfo(pt):
#Returns the patient information dictionary from the patient tuple.
#Extracts and returns the second element (index 1) of the patient tuple, which is the PatientDictionary.
    return pt[1]

"""part 2"""

def isHypertensive(age,sex,trestbps):
#checks to see if patient is hypertensive by comparing the age, sex and trestbps of the patient
#Defines hypertensive conditions for different age groups and sexes
    age = int(age)
    sex = str(sex)
    trestbps = int(trestbps)
    if (age >=1 and age <=3) and (sex=='M' or sex=='F') and (trestbps>=98):
        return True
    elif (age>=4) and (trestbps>=140) and (sex=='M' or sex=='F'):
        return True
    else:
        return False

def hasHighCholesterol(chol):
#Checks if a patient has high cholesterol based on their cholesterol level (chol).
#Defines a threshold for high cholesterol
    chol= int(chol)
    if chol>=220:
        return True
    return False

def isPhysicallyInactive(thalach,sex,age):
#Determines if a patient is physically inactive based on their maximum heart rate (thalach), sex, and age.
#Defines different criteria for males and females in different age groups.
    thalach= int(thalach)
    sex = str(sex)
    age = int(age)
    if sex == "M":
        if (age>=35) and (thalach>=220):
            return True
        elif (age<35) and (thalach>=230):
            return True
        else:
            return False
    elif sex=="F":
        if (age>=35) and (thalach>=226):
            return True
        elif (age<35) and (thalach>=236):
            return True
        else:
            return False
    else:
        return False

"""part 3"""

def makePscore(ptLst):
#Creates and returns a placeholder patient score list with the structure ['PS', []].
    return ['PS',[]]

def calPscore(pt):
#Calculates and returns a patient's risk score based on hypertensive status/
#cholesterol level, physical inactivity, and gender.
    age= getPatientAge(pt)
    sex = getPatientSex(pt)
    trestbps= getPatientTres(pt)
    cholesterol= getPatientChol(pt)
    thalach= getPatientTlach(pt)
    points=0.0
    if isHypertensive(age,sex,trestbps)==True:
        points+=4
    if hasHighCholesterol(cholesterol)==True:
        points+=3
    if isPhysicallyInactive(thalach,sex,age)==True:
        points+=2
    if (sex == 'male' or sex=='m' or sex=='M' or sex=='Male'):
        points+=1.5
    if (sex == 'female' or sex=='f' or sex=='F' or sex=='Female'):
        points+=1
    return points
    
def addPatient(PSLst,pt):
#Adds a patient and their calculated score to the patient score list (PSLst).
     if isPatient(pt):
        patientsScore= calPscore(pt)
        ptScores(PSLst).append((pt,patientsScore))

def ptScores(PSLst):
#Returns the patient score list from the patient score list structure.
    return PSLst[1]

def getCritical(Score):
#Returns a list of patients from the patient score list/
#whose scores are greater than or equal to the specified score.
    SLst=ptScores(PSLst)
    criticalPatients=[]
    for i in SLst:
          if i[1]>=Score:
            criticalPatients.append(i[0])
    return criticalPatients

def getNonCrit(Score):
#Returns a list of patients from the patient score list/
#whose scores are less than or equal to the specified score.
    SLst=ptScores(PSLst)
    notcriticalPatients=[]
    for i in SLst:
        if i[1]<=Score:
            notcriticalPatients.append(i[0])
    return notcriticalPatients


def isScore(Score):
#Checks if the input is a valid score (float) and within a specified range.
     return type(Score)==float and Score<=11.5

def isEmptyScore(Score):
#hecks if a patient score is empty.
    return Score==['PS',[]]

"""part 4"""

def makePtQueue(Qtype):
#Creates and returns a patient queue with a specified type (critical, non-critical, or watching).
     if Qtype==1:
        return('C-Q',[])
     elif Qtype == 2:
        return ('N-Q', [])
     elif Qtype == 3:
        return ('W-Q', [])
     else:
        return'ENTER 1,2 OR 3'

def contentsQ(q):
#Returns the list of patients in the patient queue.
     return q[1]

def frontPtQ(q):
#Returns the patient at the front of the patient queue.
     if isPatientQ(q) and not isEmptPtQ(q):
        queue=contentsQ(q)
        return queue[0]


def addToPtQ(pt, q):
#Adds a patient to the patient queue.
     if isPatientQ(q) and isPatient(pt):
            contentsQ(q).append(pt)
            

def removeFromPtQ(q):
#Removes a patient from the front of the patient queue.
    if not isEmptPtQ(q):
        contentsQ(q).pop(0)

def isPatientQ(q):
#Checks if the input is a valid patient queue.
     return type(q)== tuple and len(q)== 2 and type(q[0])==str

def isEmptPtQ(q):
#Checks if a patient queue is empty.
    queue= contentsQ(q)
    return len(q)==2 and queue==[]

"""part 5"""

def makePatientStack():
#Creates and returns a patient stack
     return ('HDS', [])

def contentsStack(stk):
#Returns the list of patients in the patient stack.
     return stk[1]

def topPtStack(stk):
#Returns the patient at the top of the patient stack
     if isPtStack(stk):
        stack= contentsStack(stk)
        return stack[0]

def pushPtStack(pkt, stk):
#Pushes a patient onto the patient stack.
     if isPtStack(stk):
        contentsStack(stk).insert(0,pkt)

def popPtStack(stk):
#Pops a patient from the top of the patient stack
    if isPtStack(stk):
        contentsStack(stk).pop(0)

def isPtStack(stk):
#Checks if the input is a valid patient stack.
    return type(stk)== tuple and len(stk)== 2 and stk[0]=='HDS'

def isEmptyPtStack(stk):
#Checks if a patient stack is empty.
    ptstack= contentsStack(stk)
    return len(stk)==2 and ptstack==[]

"""part 6"""


def sortPatients(ptLst,ptStk,ptQ):
#Sorts patients in both the patient stack and patient queue based on their risk scores.
     if isPtStack(ptStk) and isPatientQ(ptQ):
        contentsStack(ptStk).sort(key=lambda x:calPscore(x),reverse=True)
        contentsQ(ptQ).sort(key=lambda y:calPscore(y),reverse=True)

"""part 7"""


def analyzePatients(patient_lst):
#Analyzes the risk scores of a list of patients, creates patient objects,/
#adds them to the patient score list, and returns the final patient queue.
    plst=[]
    for i in patient_lst:
        plst.append(makePatient(*i))
    scorelst=makePscore(plst)
    for pt in plst:
        addPatient(scorelst,pt)
    plsl= list(zip(plst,contentsQ(scorelst)))
    crit=makePtQueue(1)
    for j in plst:
        addToPtQ(j,crit)
    sac=makePatientStack()
    sortPatients(plst,sac,crit)
    return contentsQ(crit)       
        
"""part 8"""       


if __name__ == '__main__':
#Takes input for the number of patients and their information, creates patient objects, and/
#analyzes and prints the final patient queue along with the risk scores of the first and last/
#patients in the queue.
    no_of_patients = int(input())
    p_lst = []
    ip_lst = []
    for i in range(no_of_patients):
        ip_info = input().strip().split()
        ip_tup = (int(ip_info[0]), ip_info[1], int(ip_info[2]), \
                  int(ip_info[3]), int(ip_info[4]), int(ip_info[5]), float(ip_info[6]))
        ip_lst += [ip_tup]
    print(ip_lst)
    p_lst = []
    for ip_info in ip_lst:
        p_lst += [makePatient(int(ip_info[0]), ip_info[1], int(ip_info[2]), \
                       int(ip_info[3]), int(ip_info[4]), int(ip_info[5]), float(ip_info[6]))]
    PSLst = makePscore(p_lst)
    for p in p_lst:
        addPatient(PSLst,p)
    finalQueue = analyzePatients(ip_lst)
    print(finalQueue)
    print(calPscore(finalQueue[-1]))
    print(calPscore(finalQueue[0]))
