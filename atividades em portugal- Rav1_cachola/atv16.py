programa 
{  	 
 	funcao inicio()  	{ 
 	 	real not1, not2, total, rav 
 	 	cadeia nome 
 	 	 
escreva ("digite o nome do aluno(a):") 
 	 	leia (nome) 
 	 	escreva ("\nPrimeira nota do aluno(a):") 
 	 	leia (not1) 
 	 	escreva ("\nSegunda nota do aluno(a):") 
 	 	leia (not2) 
 	 	total = (not1 + not2) / 2  	 	 
 	 	se (total >= 6) {  	 	 	escreva("Aprovado")}  	 	 	 
 	 	 	 	senao se (total <= 6) {  	 	 	 escreva ("recuperação")  	 	 	 escreva ("\nnota de recuperação:")  	 	 	 leia (rav)  
se (rav >= 5) { 
 	 	 	escreva ("aprovado(a)") } 
 	 	 	senao { 
 	 	 	 	escreva ("reprovado(o)") } 
 	 	 	} 
 	 	}  	} 
