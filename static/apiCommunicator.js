function creatEntry() {
    var deptNo = document.getElementById("cDeptNo");
    var deptName = document.getElementById("cDeptName");
    var location = document.getElementById("cLocation");

    fetch(`/create/${deptNo.value}/${deptName.value}/${location.value}`, {
        method: "POST"
    }).then(resp => {if (resp.redirected) window.location.href = resp.url});
}

function editEntry(deptNo) {
    // Opening the display
    var bgCover = document.getElementById("bgCover");
    bgCover.style.display = "inline";

    // Getting the input boxes
    var deptNoBox = document.getElementById("eDeptNo");
    var deptNameBox = document.getElementById("eDeptName");
    var locationBox = document.getElementById("eLocation");

    // Getting the current values
    var curDeptNo = document.getElementById(deptNo + "DeptNo");
    var curDeptName = document.getElementById(deptNo + "DeptName");
    var curLocation = document.getElementById(deptNo + "Location");

    // Setting the initial values of each input box
    deptNoBox.value = curDeptNo.innerHTML;
    deptNameBox.value = curDeptName.innerHTML;
    locationBox.value = curLocation.innerHTML;
}

function exitEdit() {
    // Closing the display
    var bgCover = document.getElementById("bgCover");
    bgCover.style.display = "none";

    // Getting the input boxes
    var deptNoBox = document.getElementById("eDeptNo");
    var deptNameBox = document.getElementById("eDeptName");
    var locationBox = document.getElementById("eLocation");

    // Getting the values of the input boxes
    let deptNo = deptNoBox.value;
    let deptName = deptNameBox.value;
    let location = locationBox.value;

    // Resetting the values of the input boxes
    deptNoBox.value = "";
    deptNameBox.value = "";
    locationBox.value = "";

    // Sending the edit request
    fetch(`/edit/${deptNo}/${deptName}/${location}`, {
        method: "POST",
        headers: [
            
        ]
    }).then(resp => {if (resp.redirected) window.location.href = resp.url});
}

function deleteEntry(deptno) {
    // Deleting the entry from the database
    fetch(`/delete/${deptno}`, {
        method: "POST"
    }).then(resp => {if (resp.redirected) window.location.href = resp.url});
}