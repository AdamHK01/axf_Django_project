$(document).ready(function(){
	var accunt =document.getElementById('accunt')
	var accunterr =document.getElementById('accunterr')
	var checkerr= document.getElementById('checkerr')

	var passerr = document.getElementById('passerr')
	var pass =document.getElementById('pass')
	var passwd =document.getElementById('passwd')
	var passwderr =document.getElementById('passwderr')

	accunt.addEventListener('focus',function(){
		accunterr.style.display='none'
		checkerr.style.display='none'
	})


	accunt.addEventListener('blur',function(){
		instr=this.value
		if (instr.length<6||instr.length>12){
		accunterr.style.display='block'
	}
	$.post('/checkuserid/',{'userid':instr},function(data){
			if(data.status=='error'){
				checkerr.style.display='block'
			}
	})

	})


	pass.addEventListener('focus',function(){
		passerr.style.display='none'
	})


	pass.addEventListener('blur',function(){
		instr=this.value
		if (instr.length<6||instr.length>16){
		passerr.style.display='block'
	}
	})



	passwd.addEventListener('focus',function(){
		passwderr.style.display='none'
	})

	passwd.addEventListener('blur',function(){
		if(pass.value!=passwd.value){
		passwderr.style.display='block'			
		}


	})




})