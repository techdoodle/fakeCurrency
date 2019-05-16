'use strict';

const request = require('request');
const fs = require('file-system');
const express = require('express')
const app = express()
const port = 3000
const spawnSync = require('child_process').spawn;
let {PythonShell} = require('python-shell')


app.get('/legit', function(req, res) {
	var qp = req.query.qp;
	console.log(qp);
	
	const http = require('http');
	const fs = require('fs');

	const file = fs.createWriteStream("./file.jpg");
	
	const request = http.get(`${qp}`, function(response) {
	var stream = response.pipe(file);

	stream.on('finish', () => {
			PythonShell.run('scan.py',null,(err)=>{
			if(err){
				console.log(err);
				res.send('true');	
			} else
			{console.log('crop done')
					
						PythonShell.run('integration.py',{ mode: 'text'},(err,message)=>{
							if(err){
								console.log('error in pranabs script'+err)			
							}
							else if (message){
								console.log(message.includes('Real'))
								if(message.includes('Real')){
									res.send("true")
								} else if(message.includes('Fake')){
									res.send("false")
								} else {
									res.send("true")
								}
								console.log(message)
								console.log('message over')
								
								
							}
							
							console.log('integration called')
						})
			}
		});
	});
	
	});
	
	//const ls=spawnSync('Python',['scan.py'])
	//console.log(ls)
	


	
	
});

app.get('/test',function(req,res){
console.log(req)
res.send('It works')
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
