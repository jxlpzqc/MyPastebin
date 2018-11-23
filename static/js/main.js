var flag = 0;

function passcheckOnclick()
{
	
	if($('#passcheck').prop('checked'))
	{
		$('#passwordbox').slideDown();
		
	}else{
		$('#passwordbox').slideUp();
	}
	
}

function cbDarOnclick()
{
	console.log(1)
	if($('#cb-dar').prop('checked'))
	{
		$('#passcheck').prop('checked',false); 
		$('#passcheck').attr("disabled",true);
		passcheckOnclick()
	}else{
		$('#passcheck').attr("disabled",false);
	}
}

function addwaring(html)
{
	$('#alert').html("");
	var str =" <div class='alert alert-warning' role='alert'>" + html + "</div> "
	$('#alert').append(str);
}

function adderror(html)
{
	$('#alert').html("");
	var str =" <div class='alert alert-danger' role='alert'>" + html + "</div> "
	$('#alert').append(str);
}

function goon()
{
	console.log(1)
	flag = 1;
	$("#main-form").submit()
}

function checkForm()
{
	if($("#input-content").val() == '')
	{
		adderror("Content Required!!")
		return false;
	}
	
	if($('#passcheck').prop('checked') && $('#input-password').val() == '' )
	{
		adderror("Password Required!!")
		return false;
	}
	
	if($('#input-poster').val() == '')
	{
		if(flag) return true;
		
		addwaring("If you don't input your name,you will send the paste in an anonymous way.<br/><button class='btn btn-danger btn-sm' onclick='goon()'>Go on Pasting</button>");
		
		return false;
	}
	return true;
	
}