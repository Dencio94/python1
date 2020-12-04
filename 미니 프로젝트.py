<!DOCTYPE html>

<html>
<head>
<meta charset="EUC-KR">
<style type="text/css">
* {
  box-sizing: border-box;
}

.header, .footer {
  background-color: black;
  color: white;
  padding: 15px;
}

.column {
  float: left;
  padding: 15px;
}

.clearfix::after {
  content: "";
  clear: both;
  display: table;
}
