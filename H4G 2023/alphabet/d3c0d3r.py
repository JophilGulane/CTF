import random, time

my_list = ["!","#","$","%","&","(",")","*",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\\","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~"," ","\n"]
list_of_alphabet = ["@cCepTaNc3","4cCes$_c0ntrO1","AdVaNc3D_peRs!st3nT_thRe4t","art1f@ct","4s&esSm3nT","BaCkd0oR","b@ckUp","b@s3l1nE","blU3to0th","80tn3t","bReaCh","BrUt3-foRc3","cHa1n_0f_cu$t0dy","cL1ckj@ck!ng","c0nf1gUr4ti0n_m@n4g3meNt","Cyb3r$ecUr1tY","d@t4_w4r3hoUse","d3c0d1ng","DEcRypTi0n","deT3ct1On","d3v$eCoPs","d16iT4l","dUe_c@r3","Du3_d1liGence","dyNam1c_t3st1nG","eNc0d1ng","EnCryPt1oN","3nDp01nT","eXecUta8l3_c0d#","eXf1ltr@ti0n","f!le_tRaN$fEr_pRoToCoL","f0r3nS!c$","f1rEw@lL","fIrmWaRe","g0v#rNanCe","gu!d3lIneS","h@ck#r","h4sH","HeUr!sTic$","h0n#ypOts","iDenTitY","!nciDenT","InJecTion","inTegR!ty","inTern3t_oF_tHiNgs","inTern3t_pRoToc0L","inTerNetWork!ng","!nveNt0ry","k1lL_ch@in","knoWl3dge_maNag#m3nt","loGic_boMb&","m4n-1n-tHe-m1Ddl3","muLt1-f@cTor_AuTh3nt1c@ti0n","m3d1a_@cCe$s_c0nTroL","MaLw4rE","m@nd4toRy_@cC#s$_c0nTroLs","m4rKup_laNgUages_Nonprogramming","m@xiMum_alLowa8le_d0wNtime","n3tw0rK","0n3-t1me_p@d","oPen_&oUrc3_$oFtWar3","paCkeT","p@s$w0rd","pH1shiNg","Pr1v@cY","qu@l1ty_0f_&eRv!ce","quErY","ran$omw@r3","rEc0v3ry","re$idUal_r1sk","r3sp0nSe","r0otK!t","ruLes_0f_enGag3m#nt","se$si0n_k3y","s0uRce_coDe_pr0gRam","sPam","$pyWar3","syMmeRr1c_#ncRypTi0n","th3fT","tH1rd_p@rtY","thr3@t_inRelLiGenCe_tHr3at","tR0j@n","vi3w-b@seD_acCes$","viRuS","VulnNeRab1l!ty","v1rTu@l","w#b_apPl!c@ti0n","wHaLinG","W1-f!","wOrM","zeRo_trUst","z3r0-d@y","ZomB1e"]
time_stamp = str(int(time.time()))

with open(time_stamp,'w+') as f:
	to_decode = open('file.txt','r').read()
	for i in range(len(to_decode)):
		if i != -1:
			char = to_decode[i]
			rand, ranb = int(random.randint(80, 100) - random.randint(30, 50) / random.randint(20, 30)), my_list.index(char)
			f.write(f"{list_of_alphabet[ranb]}\\x")