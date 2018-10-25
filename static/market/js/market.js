$(document).ready(function(){
	var  alltypebtn =document.getElementById('alltypebtn')
	var showsortbtn =document.getElementById('showsortbtn')
	var typediv =document.getElementById('typediv')
	var sortdiv=document.getElementById('sortdiv')
	typediv.style.display='none'
	sortdiv.style.display='none'

	alltypebtn.addEventListener('click',function(){
	typediv.style.display='block'
	sortdiv.style.display='none'
	})

	showsortbtn.addEventListener('click',function(){
	typediv.style.display='none'
	sortdiv.style.display='block'
	})

	typediv.addEventListener('click',function(){
	typediv.style.display='none'
	})

	sortdiv.addEventListener('click',function(){
	sortdiv.style.display='none'
	})


	//修改购物车
	var subShoppings =document.getElementsByClassName('subShopping')
	var addShoppings =document.getElementsByClassName('addShopping')

	for(var i = 0;i<addShoppings.length;i++){
		addShopping=addShoppings[i]
		addShopping.addEventListener('click',function(){
			pid=this.getAttribute('ga')
			$.post('/changecart/0/',{'productid':pid},function(data){
				if(data.status=='success'){
					//添加成功，把中间的span的HTML编程当前的数值
					//alert('************')
					document.getElementById(pid).innerHTML= data.data

					
				}else{
					if(data.data== -1){
						window.location.href='/login/'
					}
				}
			})

		})
	}


	for(var i = 0;i<subShoppings.length;i++){
		subShopping=subShoppings[i]
		subShopping.addEventListener('click',function(){
			pid=this.getAttribute('ga')
			$.post('/changecart/1/',{'productid':pid},function(data){
				if(data.status=='success'){
					//添加成功，把中间的span的HTML编程当前的数值
					document.getElementById(pid).innerHTML= data.data
					//alert('************')
					
				}else{
					if(data.data== -1){
						window.location.href='/login/'
					}
				}
			})

		})
	}
})