import cv2 as cv
import matplotlib.pyplot as plt
from util import *
import os 
import time

#load in all point_images:
point_images = {}
# for file in os.listdir(".//ContrastPoints//Raw"):
    # point_images[file[0:-4]] = cv.imread(".//ContrastPoints//Raw//" + str(file), cv.IMREAD_UNCHANGED)
    
alpha_count = {"AcornAmulet_0.png": 532,"AcornAmulet_1.png": 546,"AcornAmulet_2.png": 540,"AcornAmulet_3.png": 545,"Banana_0.png": 2256,"Banana_1.png": 2269,"Banana_2.png": 2271,"Banana_3.png": 2265,"BloodHarvester_0.png": 1834,"BloodHarvester_1.png": 1868,"BloodHarvester_2.png": 1829,"BloodHarvester_3.png": 1874,"BloodThorne_0.png": 1955,"BloodThorne_1.png": 1953,"BloodThorne_2.png": 1953,"BloodThorne_3.png": 1952,"Blueberries_0.png": 1245,"Blueberries_1.png": 1209,"Blueberries_2.png": 1247,"Blueberries_3.png": 1213,"BookOfLight_0.png": 4159,"BookOfLight_1.png": 4126,"BookOfLight_2.png": 4165,"BookOfLight_3.png": 4121,"BurningCoal_0.png": 328,"BurningCoal_1.png": 339,"BurningCoal_2.png": 340,"BurningCoal_3.png": 344,"BurningTorch_0.png": 1262,"BurningTorch_1.png": 1220,"BurningTorch_2.png": 1268,"BurningTorch_3.png": 1223,"CapOfDiscomfort_0.png": 2749,"CapOfDiscomfort_1.png": 2875,"CapOfDiscomfort_2.png": 2742,"CapOfDiscomfort_3.png": 2880,"Carrot_0.png": 1347,"Carrot_1.png": 1399,"Carrot_2.png": 1347,"Carrot_3.png": 1397,"ChippedAmethyst_0.png": 191,"ChippedAmethyst_1.png": 195,"ChippedAmethyst_2.png": 189,"ChippedAmethyst_3.png": 199,"ChippedRuby_0.png": 168,"ChippedRuby_1.png": 163,"ChippedRuby_2.png": 170,"ChippedRuby_3.png": 161,"ChippedSaphire_0.png": 170,"ChippedSaphire_1.png": 159,"ChippedSaphire_2.png": 165,"ChippedSaphire_3.png": 159,"ChippedTopaz_0.png": 116,"ChippedTopaz_1.png": 116,"ChippedTopaz_2.png": 116,"ChippedTopaz_3.png": 128,"CritWoodStaff_0.png": 1816,"CritWoodStaff_1.png": 1807,"CritWoodStaff_2.png": 1819,"CritWoodStaff_3.png": 1805,"DjinnLamp_0.png": 1867,"DjinnLamp_1.png": 1903,"DjinnLamp_2.png": 1868,"DjinnLamp_3.png": 1897,"FlawedAmethyst_0.png": 264,"FlawedAmethyst_1.png": 269,"FlawedAmethyst_2.png": 260,"FlawedAmethyst_3.png": 269,"FlawedRuby_0.png": 356,"FlawedRuby_1.png": 341,"FlawedRuby_2.png": 350,"FlawedRuby_3.png": 338,"Flute_0.png": 489,"Flute_1.png": 581,"Flute_2.png": 565,"Flute_3.png": 577,"Garlic_0.png": 1538,"Garlic_1.png": 1580,"Garlic_2.png": 1533,"Garlic_3.png": 1579,"Gloves_0.png": 928,"Gloves_1.png": 907,"Gloves_2.png": 937,"Gloves_3.png": 912,"Herbs_0.png": 1246,"Herbs_1.png": 1281,"Herbs_2.png": 1247,"Herbs_3.png": 1276,"ImpracticallyLargeGreatSword_0.png": 7980,"ImpracticallyLargeGreatSword_1.png": 8021,"ImpracticallyLargeGreatSword_2.png": 7973,"ImpracticallyLargeGreatSword_3.png": 8016,"JewleryBox_0.png": 3471,"JewleryBox_1.png": 3528,"JewleryBox_2.png": 3448,"JewleryBox_3.png": 3571,"JinxTorquilla_0.png": 2142,"JinxTorquilla_1.png": 2193,"JinxTorquilla_2.png": 2146,"JinxTorquilla_3.png": 2192,"LeatherCap_0.png": 2685,"LeatherCap_1.png": 2745,"LeatherCap_2.png": 2689,"LeatherCap_3.png": 2744,"LuckyClover_0.png": 717,"LuckyClover_1.png": 716,"LuckyClover_2.png": 711,"LuckyClover_3.png": 716,"LuckyPiggy_0.png": 2766,"LuckyPiggy_1.png": 2793,"LuckyPiggy_2.png": 2768,"LuckyPiggy_3.png": 2795,"MagicTorch_0.png": 1085,"MagicTorch_1.png": 1060,"MagicTorch_2.png": 1083,"MagicTorch_3.png": 1070,"ManaOrb_0.png": 1273,"ManaOrb_1.png": 1247,"ManaOrb_2.png": 1264,"ManaOrb_3.png": 1243,"NocturnalLockLifter_0.png": 632,"NocturnalLockLifter_1.png": 616,"NocturnalLockLifter_2.png": 645,"NocturnalLockLifter_3.png": 599,"PerfectAmethyst_0.png": 466,"PerfectAmethyst_1.png": 460,"PerfectAmethyst_2.png": 467,"PerfectAmethyst_3.png": 463,"PerfectSaphire_0.png": 488,"PerfectSaphire_1.png": 503,"PerfectSaphire_2.png": 489,"PerfectSaphire_3.png": 511,"PerfectTopaz_0.png": 481,"PerfectTopaz_1.png": 485,"PerfectTopaz_2.png": 486,"PerfectTopaz_3.png": 480,"PiercingArrow_0.png": 1542,"PiercingArrow_1.png": 1522,"PiercingArrow_2.png": 1543,"PiercingArrow_3.png": 1499,"Pineapple_0.png": 3892,"Pineapple_1.png": 3953,"Pineapple_2.png": 3882,"Pineapple_3.png": 3965,"PoisonIvy_0.png": 1017,"PoisonIvy_1.png": 1037,"PoisonIvy_2.png": 1019,"PoisonIvy_3.png": 1028,"PoisonPotion_0.png": 322,"PoisonPotion_1.png": 321,"PoisonPotion_2.png": 282,"PoisonPotion_3.png": 285,"RainbowGoobert_0.png": 6750,"RainbowGoobert_1.png": 6764,"RainbowGoobert_2.png": 6765,"RainbowGoobert_3.png": 6727,"RegularEmerald_0.png": 323,"RegularEmerald_1.png": 334,"RegularEmerald_2.png": 318,"RegularEmerald_3.png": 331,"RegularRuby_0.png": 419,"RegularRuby_1.png": 392,"RegularRuby_2.png": 429,"RegularRuby_3.png": 405,"RegularSaphire_0.png": 382,"RegularSaphire_1.png": 375,"RegularSaphire_2.png": 379,"RegularSaphire_3.png": 386,"RegularTopaz_0.png": 318,"RegularTopaz_1.png": 320,"RegularTopaz_2.png": 310,"RegularTopaz_3.png": 325,"RubyChonk_0.png": 7458,"RubyChonk_1.png": 7462,"RubyChonk_2.png": 7478,"RubyChonk_3.png": 7470,"ShieldOfValor_0.png": 14433,"ShieldOfValor_1.png": 14365,"ShieldOfValor_2.png": 14433,"ShieldOfValor_3.png": 14365,"SpikedShield_0.png": 5169,"SpikedShield_1.png": 5166,"SpikedShield_2.png": 5167,"SpikedShield_3.png": 5161,"StaminaPotion_0.png": 362,"StaminaPotion_1.png": 371,"StaminaPotion_2.png": 358,"StaminaPotion_3.png": 385,"StoneskinPotion_0.png": 515,"StoneskinPotion_1.png": 511,"StoneskinPotion_2.png": 502,"StoneskinPotion_3.png": 504,"StrongHealthPotion_0.png": 805,"StrongHealthPotion_1.png": 817,"StrongHealthPotion_2.png": 821,"StrongHealthPotion_3.png": 819,"StrongStaminaPotion_0.png": 435,"StrongStaminaPotion_1.png": 424,"StrongStaminaPotion_2.png": 433,"StrongStaminaPotion_3.png": 425,"StrongStoneskinPotionA_0.png": 120,"StrongStoneskinPotionA_1.png": 120,"StrongStoneskinPotionA_2.png": 127,"StrongStoneskinPotionA_3.png": 117,"StrongStoneskinPotion_0.png": 429,"StrongStoneskinPotion_1.png": 427,"StrongStoneskinPotion_2.png": 432,"StrongStoneskinPotion_3.png": 446,"Tim_0.png": 559,"Tim_1.png": 570,"Tim_2.png": 555,"Tim_3.png": 572,"TuskPiercer_0.png": 1407,"TuskPiercer_1.png": 1415,"TuskPiercer_2.png": 1406,"TuskPiercer_3.png": 1384,"VampireCharm_0.png": 1361,"VampireCharm_1.png": 1401,"VampireCharm_2.png": 1366,"VampireCharm_3.png": 1390,"VampireGloves_0.png": 2154,"VampireGloves_1.png": 2213,"VampireGloves_2.png": 2162,"VampireGloves_3.png": 2222,"VampiricArmor_0.png": 7373,"VampiricArmor_1.png": 7366,"VampiricArmor_2.png": 7401,"VampiricArmor_3.png": 7382,"WalrusTusk_0.png": 901,"WalrusTusk_1.png": 969,"WalrusTusk_2.png": 936,"WalrusTusk_3.png": 979,"YggdrisalLeaf_0.png": 1078,"YggdrisalLeaf_1.png": 1081,"YggdrisalLeaf_2.png": 1072,"YggdrisalLeaf_3.png": 1077}
#Manually tweak the difficulty of matching images:
for i in range(4):
    alpha_count["StoneskinPotion" + "_" + str(i) + ".png"] *= .5
    alpha_count["LuckyClover" + "_" + str(i) + ".png"] *= .3
    alpha_count["Gloves" + "_" + str(i) + ".png"] *= .3
    alpha_count["ChippedTopaz" + "_" + str(i) + ".png"] *= 1.5
    alpha_count["ChippedAmethyst" + "_" + str(i) + ".png"] *= 1.5
    alpha_count["ChippedSaphire" + "_" + str(i) + ".png"] *= 1.5
    alpha_count["ChippedRuby" + "_" + str(i) + ".png"] *= 1.5
    alpha_count["DjinnLamp" + "_" + str(i) + ".png"] *= 1.5
    alpha_count["StrongStaminaPotion" + "_" + str(i) + ".png"] *= 1.9
    alpha_count["PoisonPotion" + "_" + str(i) + ".png"] *= 2.5
    alpha_count["Tim" + "_" + str(i) + ".png"] *= 2
    alpha_count["StrongHealthPotion" + "_" + str(i) + ".png"] *= 1.8
    alpha_count["WalrusTusk" + "_" + str(i) + ".png"] *= 1.3
    alpha_count["Flute" + "_" + str(i) + ".png"] *= 1.3
    alpha_count["RegularRuby" + "_" + str(i) + ".png"] *= 1
    alpha_count["RegularTopaz" + "_" + str(i) + ".png"] *= 1
    alpha_count["RegularSaphire" + "_" + str(i) + ".png"] *= 1
    alpha_count["RegularEmerald" + "_" + str(i) + ".png"] *= 1
    alpha_count["BloodHarvester" + "_" + str(i) + ".png"] *= 3
    alpha_count["PoisonIvy" + "_" + str(i) + ".png"] *= .7
    alpha_count["VampiricArmor" + "_" + str(i) + ".png"] *= .7
    
    
img1 = cv.imread("test10.png")
img2 = cv.imread('ui_1.png') # target

sift = cv.SIFT_create(nfeatures=700000)
sift5 = cv.SIFT_create(nfeatures=50000)
foundim = find_subimage_hard(img1, img2, sift, sift5)
foundim = foundim[35:585,5:-25,:]

cv.imwrite("foundim.png", foundim)
boardWidth, boardHeight = foundim.shape[:2]
plt.imshow(foundim)
plt.show()

board_map = []

# for i in range(boardWidth):
    # board_map.append([])
    # for j in range(boardHeight):
        # board_map[i].append(None)
        
# start = time.time()
# for pointImgKey in point_images:
    # imgStart = time.time()
    # template = point_images[pointImgKey]
    # base = template[:,:,0:3]    
    # alpha = template[:,:,3]
    # alpha = cv.merge([alpha, alpha, alpha])
    # res = cv.matchTemplate(foundim,base,method=cv.TM_SQDIFF,mask=alpha)
    # postMatch = time.time()
    # #print("match time: " + str(postMatch - imgStart))
    # res = np.array(res)
    # b,c = np.where(res<4000)
    # for i in range(c.shape[0]):
        # cv.imwrite(".//contrastPoints//wtfImIFinding//" + pointImgKey + ".png", foundim[b[i]:b[i]+3,c[i]:c[i]+3])
    
    #print("search time: " + str(time.time() - postMatch))
  
                
                

# #----------------------------------------------------------------------------------------------------------------------------------------
packCord0 = []
packCord1 = []
for i in range(7):
    packCord0.append([])
    packCord1.append([])
    for j in range(9):
        packCord0[i].append(None)
        packCord1[i].append(None)



#TM_CCOEFF_NORMED
found = []
start = time.time()
fig, ax = plt.subplots()
toggle = True
ax.imshow(foundim)
for file in os.listdir(".//target_images//FilledRaw"):
    t1 = time.time()
    template = cv.imread(".//target_images//FilledRaw//" + str(file), cv.IMREAD_UNCHANGED)                              
    base = template[:,:,0:3]
    alpha = template[:,:,3]
    alpha = cv.merge([alpha, alpha, alpha])
    res = cv.matchTemplate(foundim,base,method=cv.TM_SQDIFF,mask=alpha)
    templateWidth, templateHeight = template.shape[:2]
    res = np.array(res)
    res /= alpha_count[str(file)]
    b,c = np.where(res < 2500)
    #b,c = np.where(res>.7)
    
    for ii in range(c.shape[0]):
        i = b[ii]
        j = c[ii]
        t0 = time.time()
        targ = (j, i)
        box = plt.Rectangle(targ, templateHeight, templateWidth, fill=False, color='white')
        ax.add_patch(box)
        ax.text(targ[0], targ[1], str(file))
        

               
    
print("-------------------------------------------")
print(time.time() - start)

# print(packCord0)
# print(packCord1)
        
plt.show()

    
    


    #print(target_matched_points)