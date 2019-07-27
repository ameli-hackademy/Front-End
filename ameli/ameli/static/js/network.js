var DIR = 'icon/';

var nodes = null;
var edges = null;
var network = null;

var title1 = "<div class='card border-light' style='width: 8rem;height:6rem;'><div class='card-body'><p>SENT ：20</p><p>RECEIVED ：33</p></div></div>"


// Called when the Visualization API is loaded.
function draw() {
  // create people.
  // value corresponds with the age of the person
  var DIR = '../hackathon/icon/';
  nodes = [
    {id: 1,  shape: 'circularImage', image: DIR + '1.png',size:70},
    {id: 2,  shape: 'circularImage', image: DIR + '2.png',size:50},
    {id: 3,  shape: 'circularImage', image: DIR + '3.png',size:50},
    {id: 4,  shape: 'circularImage', image: DIR + '4.png', label:"Black Panther",size:50,title:title1},
    {id: 5,  shape: 'circularImage', image: DIR + '5.png',size:50},
    {id: 6,  shape: 'circularImage', image: DIR + '6.png',size:50},
    {id: 7,  shape: 'circularImage', image: DIR + '7.png'},
    {id: 8,  shape: 'circularImage', image: DIR + '8.png'},
    {id: 9,  shape: 'circularImage', image: DIR + '9.png'},
    {id: 10, shape: 'circularImage', image: DIR + '10.png'},
    {id: 11, shape: 'circularImage', image: DIR + '11.png'}
  ];

  // create connections between people
  // value corresponds with the amount of contact between two people
  edges = [
    {from: 1, to: 2,length:200},
    {from: 1, to: 3,length:200},
    {from: 1, to: 4,length:200},
    {from: 1, to: 5,length:200},
    {from: 1, to: 6,length:200},
    {from: 1, to: 7,length:300},
    {from: 1, to: 8,length:300},
    {from: 1, to: 9,length:300},
    {from: 1, to: 10,length:300},
    {from: 1, to: 11,length:300}
  ];

  // create a network
  var container = document.getElementById('mynetwork');
  var data = {
    nodes: nodes,
    edges: edges
  };
  var options = {
    autoResize:true,
    nodes: {
      borderWidth:5,
      size:40,
    color: {
        border: '#222222',
        background: '#666666'
      },
      font:{color:'black'}
    },
    edges: {
      color: 'lightgray',
      width:2
    },

  };
  network = new vis.Network(container, data, options);
}
