/* Add your Application JavaScript */
const Home = {
  name: 'Home',
  template: `
  <div class="home">
    <img src="/static/images/logo.png" alt="VueJS Logo">
    <h1>{{ welcome }}</h1>
  </div>
  `,
  data() {
    return {
      welcome: 'Hello World! Welcome to VueJS'
    }
  }
 };

 const carlist = {
  name: 'carlist',
  template: 
    `
    <div class="cars">
      <h2>Explore</h2>
	  <ul class="carlist">
		  <div id="searchbox" class="form-inline d-flex">
		  
		  
			<div id="makebox">
			  <label id="makelabel">Make</label>
			  <input type="search" id="input1" name="make" class="form-control mb-2 mr-sm-2"/>
			</div>
			<div id="label-box">
			  <label id="model-label">Model</label>
			  <input type="search" id="input2" name="model" class="form-control mb-2 mr-sm-2" />
			</div>
			<button id="btn" class="form-control mb-2 mr-sm-2">Search</button>

		  </div>  
			<div class ="info">
			  
			  <li class="carinfo" v-for="(n,i) in cardetails.length">
				<img v-bind:src ="'{{ carimglist[i] }}'"><br>
				<b id="cd">{{ cardetails[i].year }}</b>
				<b>{{ cardetails[i].make }}</b>
				<div id="price"><img id="ppic" alt="price pic" src ="/static/images/price-tag-icon.png">  {{ cardetails[i].price }}</div>
				<p id="cd">{{ cardetails[i].model }}</p>
				
				<button id="detailbtn">View more details</button>
			  </li>
			</div>      
	  </ul>
    </div
  `,
    created() {
      let self = this;
      fetch('/api/cars', {
                method: 'GET'
               })
 
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      console.log(data);
      self.cardetails = data.cardetails;
	  self.carimglist = data.carimglist;
    });
    },
   
  data(){
    return{
		cardetails:[],
		carimglist:[]
	}
	
  }/*,
  methods: {
    displaycar() {
      let self = this;
      fetch('/api/cars', {
                method: 'GET'
               })
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        console.log(data);
        self.cardetails = data.cardetails;

      });
    }
  }*/

};


const app = Vue.createApp({
  data() {
    return {
      welcome: 'Hello World! Welcome to VueJS'
    }
  },
  components: {
    'home': Home,
    'cars': carlist
  }
});

const router = VueRouter.createRouter({
  history: VueRouter.createWebHistory(),routes: [{ path: '/', component: Home },{ path: '/api/cars', component: carlist }]
});

app.component('app-header', {
  name: 'AppHeader',
  template: `
      <header>
          <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
            <a class="navbar-brand" href="#">VueJS App</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                  <router-link to="/" class="nav-link">Home</router-link>
                </li>
                <li class="nav-item">
                  <router-link to="/api/cars" class="nav-link">Explore</router-link>
                </li>
              </ul>
            </div>
          </nav>
      </header>    
  `,
  data: function() {
    return {};
  }
});




app.component('app-footer', {
  name: 'AppFooter',
  template: `
      <footer>
          <div class="container">
              <p>Copyright &copy {{ year }} Flask Inc.</p>
          </div>
      </footer>
  `,
  data: function() {
      return {
          year: (new Date).getFullYear()
      }
  }
});
 
app.use(router)

app.mount('#app');