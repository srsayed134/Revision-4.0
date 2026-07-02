// Example of DSA 

//This is data structure
/*
const studentsDatabase = ["Jordan", "Erick", "Jhon","Michel"];
//This is algorithm to found specific data
const findStudent = (allStudent, studentName) => {
    for(let i = 0; i < allStudent.length; i++){
        if(allStudent[i] === studentName){
            console.log(`${studentName} found`)
            return;
        }
    }
    console.log(`${studentName} is not found`)
}
findStudent(studentsDatabase, "Sayed")
*/
// Big O notation
//BigO notation helps us understand how long an algorithm will 
// take to run or how much memory it will need as ther amount of data 
// it handles grows

//O(n)
// Signifies that the execution time of the algorithm grows linearly 
// in proportion to the size of the input data (n)

// Example  of O(n)
/*
const groceries = ["Milk", "Bread", "Egg", "Oil", "Icecreame", "Suger"];

const findProdunct = (groceriesitem, item) => {
    for(let i = 0; i < groceriesitem.length; i++){
        if(groceries[i] === item){
            console.log(`${item} is found`)
        }
    }
    //Example of O(2n) but O(n)
    for(let j = 0; j< groceriesitem.length; j++){
        if(groceriesitem[j] === item){
            console.log(`${item} also found`)
        }
    }
    // n + n = 2n
    //Drop the constant so it becomes O(n)
}

findProdunct(groceries, "Egg")
*/