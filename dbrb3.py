#PM_H = 500.4
#PM_M = 35.5
#PM_L = 0.0
 
AQI_H = 500.0
AQI_M = 101.0  
AQI_L = 0.0    
 
numberOfAntAttributes = 2
#relativeWeight = 1.0   
 
cbd_0 = 1.0
cbd_1 = 0.0  
cbd_2 = 0.0 
cbd_3 = 0.0 
cbd_4 = 1.0
cbd_5 = 0.0  
cbd_6 = 0.0
cbd_7 = 0.0
cbd_8 = 1.0

aqi1 = 1.0
aqi2 = 1.0  
aqi3 = 1.0
aqi4 = 1.0 
aqi5 = 1.0     
  
def ruleBase(s,c,x):  
    global consequentBeliefDegree
    #global relativeWeight1
    #global relativeWeight2
    temp_consequentBeliefDegree = [x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19], x[20], x[21], x[22], x[23], x[24], x[25], x[26]]    
       
    de0 = x[0]/(x[0] + x[1] + x[2])
    de1 = x[1]/(x[0] + x[1] + x[2])
    de2 = x[2]/(x[0] + x[1] + x[2])
    de3 = x[3]/(x[3] + x[4] + x[5]) 
    de4 = x[4]/(x[3] + x[4] + x[5])
    de5 = x[5]/(x[3] + x[4] + x[5])
    de6 = x[6]/(x[6] + x[7] + x[8])
    de7 = x[7]/(x[6] + x[7] + x[8])
    de8 = x[8]/(x[6] + x[7] + x[8])
    de9 = x[9]/(x[9] + x[10] + x[11])
    de10 = x[10]/(x[9] + x[10] + x[11])
    de11 = x[11]/(x[9] + x[10] + x[11]) 
    de12 = x[12]/(x[12] + x[13] + x[14]) 
    de13 = x[13]/(x[12] + x[13] + x[14])
    de14 = x[14]/(x[12] + x[13] + x[14])
    de15 = x[15]/(x[15] + x[16] + x[17])
    de16 = x[16]/(x[15] + x[16] + x[17])
    de17 = x[17]/(x[15] + x[16] + x[17])
    de18= x[18]/(x[18] + x[19] + x[20])
    de19 = x[19]/(x[18] + x[19] + x[20])   
    de20 = x[20]/(x[18] + x[19] + x[20])
    de21 = x[21]/(x[21] + x[22] + x[23])
    de22 = x[22]/(x[21] + x[22] + x[23])
    de23 = x[23]/(x[21] + x[22] + x[23])
    de24 = x[24]/(x[24] + x[25] + x[26])
    de25 = x[25]/(x[24] + x[25] + x[26])
    de26 = x[26]/(x[24] + x[25] + x[26])  
         
    consequentBeliefDegree = [de0, de1, de2, de3, de4, de5, de6, de7, de8, de9, de10, de11, de12, de13, de14, de15, de16, de17, de18, de19, de20, de21, de22, de23, de24, de25, de26]    
    attrw1 = x[27]  
    attrw2 = x[28]
    irulewt1 = x[29]  
    irulewt2 = x[30]  
    irulewt3 = x[31]
    irulewt4 = x[32]
    irulewt5 = x[33]
    irulewt6 = x[34]
    irulewt7 = x[35]
    irulewt8 = x[36]
    irulewt9 = x[37]

    #transformInput1(384.5891688061617)  
    PMH = 0 + (x[38] * 499.4)     #500.4     
    PMM = 0 + (x[39] * 499.4)     #35.5
    PML = 0 + (x[40] * 499.4)     #0    
    transformInput1(s,PMH,PMM,PML)   
    transformInput2(c,PMH,PMM,PML)       
    calculateMatchingDegreeBrbCnn(attrw1,attrw2, irulewt1, irulewt2, irulewt3, irulewt4, irulewt5, irulewt6, irulewt7, irulewt8, irulewt9)    
    showActivationWeight() 
    updateBeliefDegree() 
    result = aggregateER_BrbCnn()
    return result     
 
def transformInput1(i,j,k,l):   
    global H1 
    global M1 
    global L1 
            
    PM_H = j
    PM_M = k 
    PM_L = l
       
    print("Inside transformInput1() Input is ",i,"PM_H ", PM_H,"PM_M ",PM_M," PM_L ",PM_L)
      
    if (i >= PM_H): 
        H1 = 1 
        M1 = 0
        L1 = 0

    elif (i == PM_M):
        H1 = 0 
        M1 = 1
        L1 = 0
 
    elif (i <= PM_L):
        H1 = 0
        M1 = 0
        L1 = 1
       
    elif (i <= PM_H) and (i >= PM_M):
        M1 = (PM_H-i)/(PM_H-PM_M)
        H1 = 1 - M1
        L1 = 0.0 

    elif (i <= PM_M) and (i >= PM_L):
        L1 = (PM_M-i)/(PM_M-PM_L)
        M1 = 1 - L1  
        H1 = 0.0
    print("Inside transformInput1(), H1", H1, "M1 ",M1,"L1 ", L1)

def transformInput2(i,j,k,l):
    global H2   
    global M2 
    global L2
            
    PM_H = j
    PM_M = k 
    PM_L = l
       
    print("Inside transformInput2() Input is ",i) 
       
    if (i >= PM_H): 
        H2 = 1 
        M2 = 0 
        L2 = 0

    elif (i == PM_M):
        H2 = 0 
        M2 = 1 
        L2 = 0
  
    elif (i <= PM_L):
        H2 = 0
        M2 = 0
        L2 = 1
        
    elif (i <= PM_H) and (i >= PM_M):
        M2 = (PM_H-i)/(PM_H-PM_M)
        H2 = 1 - M2
        L2 = 0.0 

    elif (i <= PM_M) and (i >= PM_L):
        L2 = (PM_M-i)/(PM_M-PM_L)
        M2 = 1 - L2  
        H2 = 0.0   
    
    print("Inside transformInput2(), H2", H2, "M2 ",M2,"L2 ", L2) 

def calculateMatchingDegreeBrbCnn(aw1,aw2,irw1,irw2,irw3, irw4, irw5, irw6, irw7, irw8, irw9): 
    antattrw1 = aw1 
    antattrw2 = aw2
    global initialRuleWeight       
    initialRuleWeight = [irw1, irw2, irw3, irw4, irw5, irw6, irw7, irw8, irw9]     
    increment = 0     
    global matchingDegree 
    matchingDegree = [1.51] * 9  

    ti1 = [H1, M1, L1]  
    #print("ti1[0] is ")          
    #print(ti1[0])  
    #ti2 = array.array('f', [normalized_cnn_severe_degree, normalized_cnn_mild_degree, normalized_cnn_nominal_degree])
    ti2 = [H2, M2, L2] 
    ## Conj 
    for c in range(3):   
        for d in range(3):
            #print(ti1[c])  
            matchingDegree[increment] = initialRuleWeight[increment] * (ti1[c] ** antattrw1) * (ti2[d] ** antattrw2)     
            #trainedMatchingDegree[increment] = (ti1[c] ** relativeWeight) + (ti2[c] ** relativeWeight)
            increment +=1  
    ##Conj    
    print("Inside calculateMatchingDegreeBrbCnn() relativeWeight1 ",antattrw1,"relativeWeight2 ",antattrw2)   
    #print("Inside calculateMatchingDegreeBrbCnn() best9 relativeWeight1 ",best[9]," best10 relativeWeight2 ",best[10])     
def showActivationWeight():    
    trace = 1           
    totalWeight = 0 
    totalActivationWeight = 0   
    global activationWeight  
    activationWeight = [1.51] * 9        
    for x in range(9):    
        totalWeight += matchingDegree[x]           
        
    ##Conj
    for counter in range(9):            
        inter = matchingDegree[counter]  
        activationWeight[counter] = inter/totalWeight      
    ##Conj        

def updateBeliefDegree():
    update = 0
    sumAntAttr1 = 1
    sumAntAttr2 = 1  
    
    if (H1 + M1 + L1) < 1:
        sumAntAttr1 = H1 + M1 + L1
        update = 1 
      
    if (H2 + M2 + L2) < 1:
        sumAntAttr2 = H2 + M2 + L2
        update = 1 
     
    if update == 1:
        beliefDegreeChangeLevel = (sumAntAttr1 + sumAntAttr2)/numberOfAntAttributes 

        for go in range(27): 
            consequentBeliefDegree[go] = beliefDegreeChangeLevel * consequentBeliefDegree[go]
    else: 
        print ("No upgradation of belief degree required.") 
def aggregateER_BrbCnn():   
    parse = 0
    move1 = 0 
    move2 = 1  
    move3 = 2 
    action1 = 0
    action2 = 1
    action3 = 2 
    
    global ruleWiseBeliefDegreeSum 
    ruleWiseBeliefDegreeSum = [1.51] * 9 
    
    part11 = 1.51
    part12 = 1.51
    part13 = 1.51
    
    part1 = 1.0
    part2 = 1.0
    value = 1.0
    meu = 1.0
    
    numeratorH1 = 1.0
    numeratorH2 = 1.0
    numeratorH = 1.0
    denominatorH1 = 1.0
    denominatorH = 1.0
    
    numeratorM1 = 1.0  
    numeratorM = 1.0
    
    numeratorL1 = 1.0
    numeratorL = 1.0
     
    utilityScoreH = 1.0
    utilityScoreM = 0.5
    utilityScoreL = 0.0
    crispValue = 1.0
    degreeOfIncompleteness = 1.0
    utilityMax = 1.0 
    utilityMin = 1.0
    utilityAvg = 1.0
    
    global aqi
    
    for s in range(27): 
        print("Inside aggregateER)BrbCNN() consequentBeliefDegree: ",consequentBeliefDegree[s])
     
    for t in range(9): 
        parse = t * 3   
        ruleWiseBeliefDegreeSum[t] = consequentBeliefDegree[parse] + consequentBeliefDegree[parse+1] + consequentBeliefDegree[parse+2]
 
    for rule in range(9):  
        part11 *= (activationWeight[rule] * consequentBeliefDegree[move1] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))         
        move1 += 3 
  
    for rule in range(9):
        part12 *= (activationWeight[rule] * consequentBeliefDegree[move2] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        move2 += 3 
 
    for rule in range(9):
        part13 *= (activationWeight[rule] * consequentBeliefDegree[move3] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        move3 += 3

    part1 = (part11 + part12 + part13)
    
    for rule in range(9):
        part2 *= (1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule])) 
    
    value = part1 - part2 
    
    meu = 1/value 
 
    for rule in range(9):
        numeratorH1 *= (activationWeight[rule] * consequentBeliefDegree[action1] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        action1 += 3

    for rule in range(9):
        numeratorH2 *= (1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))              
      
    numeratorH = meu * (numeratorH1 - numeratorH2) 
    
    for rule in range(9):  
        denominatorH1 *= (1 - activationWeight[rule])        
 
    denominatorH = 1 - (meu * denominatorH1)
    
    aggregatedBeliefDegreeH = (numeratorH/denominatorH)
    
    for rule in range(9):
        numeratorM1 *= (activationWeight[rule] * consequentBeliefDegree[action2] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        action2 += 3 

    numeratorM = meu * (numeratorM1 - numeratorH2) 
    aggregatedBeliefDegreeM = (numeratorM/denominatorH)  
    
    for rule in range(9):
        numeratorL1 *= (activationWeight[rule] * consequentBeliefDegree[action3] + 1 - (activationWeight[rule] * ruleWiseBeliefDegreeSum[rule]))        
        action3 += 3
     
    numeratorL = meu * (numeratorL1 - numeratorH2)
    aggregatedBeliefDegreeL = (numeratorL/denominatorH) 
    
    if (aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL) == 1:
        crispValue = (aggregatedBeliefDegreeH * utilityScoreH) + (aggregatedBeliefDegreeM * utilityScoreM) + (aggregatedBeliefDegreeL * utilityScoreL)
        brbH = aggregatedBeliefDegreeH
        brbM = aggregatedBeliefDegreeM
        brbL = aggregatedBeliefDegreeL       
        
        print ("\n BRB-CNN integrated Belief Degree for Hazardous AQI: ",aggregatedBeliefDegreeH,"\n")
        print ("\n BRB-CNN integrated Belief Degree for Unhealthy AQI: ",aggregatedBeliefDegreeM,"\n")
        print ("\n BRB-CNN integrated Belief Degree for Good AQI: ",aggregatedBeliefDegreeL,"\n")
        #cout << "brbH: " << brbH << " brbM: " << brbM << " brbL: " << brbL <<endl;    
 
    else:         
        degreeOfIncompleteness = 1 - (aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL)
        
        utilityMax = ((aggregatedBeliefDegreeH + degreeOfIncompleteness) * utilityScoreH + (aggregatedBeliefDegreeM*utilityScoreM) + (aggregatedBeliefDegreeL*utilityScoreL))
        
        utilityMin = (aggregatedBeliefDegreeH*utilityScoreH) + (aggregatedBeliefDegreeM*utilityScoreM) + (aggregatedBeliefDegreeL + degreeOfIncompleteness) * utilityScoreL
        
        utilityAvg = (utilityMax + utilityMin)/2  
         
        print ("BRB-CNN integrated Belief Degrees considering degree of Incompleteness: ")  
        
        finalAggregatedBeliefDegreeH = aggregatedBeliefDegreeH/(aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL)  
         
        finalAggregatedBeliefDegreeM = aggregatedBeliefDegreeM/(aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL)
        
        finalAggregatedBeliefDegreeL = aggregatedBeliefDegreeL/(aggregatedBeliefDegreeH + aggregatedBeliefDegreeM + aggregatedBeliefDegreeL) 
          
        brbH = finalAggregatedBeliefDegreeH
        brbM = finalAggregatedBeliefDegreeM 
        brbL = finalAggregatedBeliefDegreeL       
            
        if (finalAggregatedBeliefDegreeH > finalAggregatedBeliefDegreeM) and (finalAggregatedBeliefDegreeH > finalAggregatedBeliefDegreeL):
            aqi = (201 + 299*finalAggregatedBeliefDegreeH) + ((200*finalAggregatedBeliefDegreeM)/2)
            print ("AQI predicted by BRB-CNN:",aqi)    
            
        elif (finalAggregatedBeliefDegreeL > finalAggregatedBeliefDegreeM) and (finalAggregatedBeliefDegreeL > finalAggregatedBeliefDegreeH): 
            aqi = (100*(1 - finalAggregatedBeliefDegreeL)) + ((200*finalAggregatedBeliefDegreeM)/2) 
            print ("AQI predicted by BRB-CNN:",aqi)
  
        elif (finalAggregatedBeliefDegreeM > finalAggregatedBeliefDegreeH) and (finalAggregatedBeliefDegreeM > finalAggregatedBeliefDegreeL):
            if finalAggregatedBeliefDegreeH > finalAggregatedBeliefDegreeL:
                aqi = (101 + 99*finalAggregatedBeliefDegreeM) + ((500*finalAggregatedBeliefDegreeH)/2)
                print ("AQI predicted by BRB-CNN: ",aqi)
      
            elif (finalAggregatedBeliefDegreeL > finalAggregatedBeliefDegreeH):   
                aqi = (101 + 99*finalAggregatedBeliefDegreeM) + ((100*finalAggregatedBeliefDegreeL)/2)
                print ("AQI predicted by BRB-CNN:",aqi)  
          
        print("aqi ",aqi)      
                
        if aqi >= 301: 
            aqi6 = (aqi- 301)/199.0  
 
        elif (aqi >= 201)and (aqi <= 300.9999999999): 
            aqi6 = (aqi- 201)/99.0     

        elif (aqi >= 151)and (aqi <= 200.9999999999):
            aqi6 = (aqi- 151)/49.0 

        elif((aqi >= 101)and (aqi <= 150.9999999999)): 
            aqi6 = (aqi- 101)/49.0   

        elif((aqi >= 51)and (aqi <= 100.9999999999)): 
            aqi6 = (aqi- 51)/49.0    
 
        elif(aqi <= 50.9999999999):    
            aqi6 = (aqi/49.0)    
             
        print("aqi6 ",aqi6) 
        print ("BRB-CNN integrated Belief Degree for Hazardous AQI:",finalAggregatedBeliefDegreeH*aqi6)   
        print ("BRB-CNN integrated Belief Degree for Very Unhealthy AQI:",finalAggregatedBeliefDegreeH*(1-aqi6)) 
        print ("BRB-CNN integrated Belief Degree for Unhealthy AQI: ",finalAggregatedBeliefDegreeM*aqi6)
        print ("BRB-CNN integrated Belief Degree for Unhealthy (Sensitive Groups) AQI:",finalAggregatedBeliefDegreeM*(1-aqi6)) 
        print ("BRB-CNN integrated Belief Degree for Moderate AQI:",finalAggregatedBeliefDegreeL*aqi6) 
        print ("BRB-CNN integrated Belief Degree for Good AQI:",finalAggregatedBeliefDegreeL*(1-aqi6))
        
        return aqi