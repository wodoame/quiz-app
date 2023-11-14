fetch("/get-questions/?year=2018&subject=science").then(
    response=>response.json()
).then(data=>console.log(data))