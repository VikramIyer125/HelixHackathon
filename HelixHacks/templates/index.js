
getCoViDData();
  async function getCoViDData(){
   var fileName = "/covidapp.csv";
    
    
  
   const response = await fetch(fileName);
   const data = await response.text();
   const rows = data.split('\n');

    rows.forEach(elt => {
      const row = elt.split(',');
      var state = parseString(row[0]);
      var name = parseString(row[1]);
      var address = parseString(row[2]);
      var city  = parseString(row[3]);
      var facility = parseString(row[4]);
      var hours = parseString(row[5]);
      var phonenumber = parseString(row[6]);
      var eligibility = parseString(row[7]);

    });
  }



