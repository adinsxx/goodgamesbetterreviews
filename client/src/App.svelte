<script>
	let rand = -1;
	function getRand() {
	  fetch("./rand")
		.then(c => c.text())
		.then(c => (rand = c));
	}
	let pic_link = "https://images.heb.com/is/image/HEBGrocery/prd-small/h-e-b-bakery-asiago-cheese-bread-scratch-made-001121246.jpg"
	let button_text = "banana"
	function getpic() {
		if (button_text == "banana") {
			fetch("./getbanana")
			.then(bread => bread.text())
			.then(bread => (pic_link = bread))
			button_text = "bread"

		} else {
			fetch("./getbread")
			.then(banana => banana.text())
			.then(banana => (pic_link = banana))
			button_text = "banana"
		}


	}
  </script>
  
  <img src={pic_link} alt="banana?">
  <button on:click={getpic}>{button_text}</button>
 



