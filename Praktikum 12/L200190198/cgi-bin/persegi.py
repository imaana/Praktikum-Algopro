print("<!DOCTYPE html>")
print("<html>
<head>
<title>Bangun Geometri</title>
<script type="text/javascript">
function hitung(op){
var bil1 = parseFloat(document.formku.bil1.value);
var hasil;
if (op=="Hitung")
hasil = bil1*bil1;
else hasil = " ";
document.formku.result.value=hasil;}
</script>
</head>

<body>")
print("<h1>Bangun Geometri</h1>")
print("<form name="formku">")
print("<table>")
print("<tr>
<td>Nama Bangun</td>
<td>:</td>
<td>Persegi</td></tr>
<tr>
<td>Dimensi(2D/3D)</td>
<td>:</td>
<td>2 Dimensi</td></tr>
<tr>
<td>Rumus Luas</td>
<td>:</td>
<td>sisi x sisi</td></tr>
<tr>
<td>Parameter 1(sisi)</td>
<td>:</td>
<td><input type="text"name="bil1"></input></td></tr>
<tr>
<td>Luas</td>
<td>:</td>")
print("<td><input type="text"name="result"></input></td></tr>")

print("<tr>")
print("<td><input type="button" value="Hitung" onclick="hitung('Hitung')"></input></td></tr>")
print("</table>")
print("</form>")

print("</body>")
print("</html>")
