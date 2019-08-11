(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-da735daa"],{"11e9":function(t,e,i){var n=i("52a7"),a=i("4630"),r=i("6821"),o=i("6a99"),s=i("69a8"),c=i("c69a"),l=Object.getOwnPropertyDescriptor;e.f=i("9e1e")?l:function(t,e){if(t=r(t),e=o(e,!0),c)try{return l(t,e)}catch(i){}if(s(t,e))return a(!n.f.call(t,e),t[e])}},"169a":function(t,e,i){"use strict";i("368e");var n=i("4ad4"),a=i("b848"),r=i("75eb"),o=i("e707"),s=i("e4d3"),c=i("21be"),l=i("f2e7"),u=i("a293"),d=i("80d2"),f=i("bfc5"),h=i("58df"),v=Object.assign||function(t){for(var e=1;e<arguments.length;e++){var i=arguments[e];for(var n in i)Object.prototype.hasOwnProperty.call(i,n)&&(t[n]=i[n])}return t};function b(t,e,i){return e in t?Object.defineProperty(t,e,{value:i,enumerable:!0,configurable:!0,writable:!0}):t[e]=i,t}var m=Object(h["a"])(n["a"],a["a"],r["a"],o["a"],s["a"],c["a"],l["a"]);e["a"]=m.extend({name:"v-dialog",directives:{ClickOutside:u["a"]},props:{dark:Boolean,disabled:Boolean,fullscreen:Boolean,fullWidth:Boolean,light:Boolean,maxWidth:{type:[String,Number],default:"none"},noClickAnimation:Boolean,origin:{type:String,default:"center center"},persistent:Boolean,scrollable:Boolean,transition:{type:[String,Boolean],default:"dialog-transition"},width:{type:[String,Number],default:"auto"}},data:function(){return{activatedBy:null,animate:!1,animateTimeout:-1,isActive:!!this.value,stackMinZIndex:200}},computed:{classes:function(){var t;return t={},b(t,("v-dialog "+this.contentClass).trim(),!0),b(t,"v-dialog--active",this.isActive),b(t,"v-dialog--persistent",this.persistent),b(t,"v-dialog--fullscreen",this.fullscreen),b(t,"v-dialog--scrollable",this.scrollable),b(t,"v-dialog--animated",this.animate),t},contentClasses:function(){return{"v-dialog__content":!0,"v-dialog__content--active":this.isActive}},hasActivator:function(){return Boolean(!!this.$slots.activator||!!this.$scopedSlots.activator)}},watch:{isActive:function(t){t?(this.show(),this.hideScroll()):(this.removeOverlay(),this.unbind())},fullscreen:function(t){this.isActive&&(t?(this.hideScroll(),this.removeOverlay(!1)):(this.showScroll(),this.genOverlay()))}},beforeMount:function(){var t=this;this.$nextTick(function(){t.isBooted=t.isActive,t.isActive&&t.show()})},beforeDestroy:function(){"undefined"!==typeof window&&this.unbind()},methods:{animateClick:function(){var t=this;this.animate=!1,this.$nextTick(function(){t.animate=!0,window.clearTimeout(t.animateTimeout),t.animateTimeout=window.setTimeout(function(){return t.animate=!1},150)})},closeConditional:function(t){var e=t.target;return!(!this.isActive||this.$refs.content.contains(e))&&(this.$emit("click:outside"),this.persistent?(this.noClickAnimation||this.overlay!==e||this.animateClick(),!1):this.activeZIndex>=this.getMaxZIndex())},hideScroll:function(){this.fullscreen?document.documentElement.classList.add("overflow-y-hidden"):o["a"].options.methods.hideScroll.call(this)},show:function(){!this.fullscreen&&!this.hideOverlay&&this.genOverlay(),this.$refs.content.focus(),this.bind()},bind:function(){window.addEventListener("focusin",this.onFocusin)},unbind:function(){window.removeEventListener("focusin",this.onFocusin)},onKeydown:function(t){if(t.keyCode===d["r"].esc&&!this.getOpenDependents().length)if(this.persistent)this.noClickAnimation||this.animateClick();else{this.isActive=!1;var e=this.getActivator();this.$nextTick(function(){return e&&e.focus()})}this.$emit("keydown",t)},onFocusin:function(t){if(t){var e=t.target;if(e&&![document,this.$refs.content].includes(e)&&!this.$refs.content.contains(e)&&this.activeZIndex>=this.getMaxZIndex()&&!this.getOpenDependentElements().some(function(t){return t.contains(e)})){var i=this.$refs.content.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');i.length&&i[0].focus()}}}},render:function(t){var e=this,i=[],n={class:this.classes,ref:"dialog",directives:[{name:"click-outside",value:function(){e.isActive=!1},args:{closeConditional:this.closeConditional,include:this.getOpenDependentElements}},{name:"show",value:this.isActive}],on:{click:function(t){t.stopPropagation()}},style:{}};this.fullscreen||(n.style={maxWidth:"none"===this.maxWidth?void 0:Object(d["e"])(this.maxWidth),width:"auto"===this.width?void 0:Object(d["e"])(this.width)}),i.push(this.genActivator());var a=t("div",n,this.showLazyContent(this.getContentSlot()));return this.transition&&(a=t("transition",{props:{name:this.transition,origin:this.origin}},[a])),i.push(t("div",{class:this.contentClasses,attrs:v({role:"document",tabindex:0},this.getScopeIdAttrs()),on:{keydown:this.onKeydown},style:{zIndex:this.activeZIndex},ref:"content"},[this.$createElement(f["a"],{props:{root:!0,light:this.light,dark:this.dark}},[a])])),t("div",{staticClass:"v-dialog__container",attrs:{role:"dialog"},style:{display:!this.hasActivator||this.fullWidth?"block":"inline-block"}},i)}})},"214c":function(t,e,i){},"368e":function(t,e,i){},"456d":function(t,e,i){var n=i("4bf8"),a=i("0d58");i("5eda")("keys",function(){return function(t){return a(n(t))}})},"4bd4":function(t,e,i){"use strict";i("214c");var n=i("3206"),a=Object.assign||function(t){for(var e=1;e<arguments.length;e++){var i=arguments[e];for(var n in i)Object.prototype.hasOwnProperty.call(i,n)&&(t[n]=i[n])}return t};e["a"]=Object(n["b"])("form").extend({name:"v-form",inheritAttrs:!1,props:{value:Boolean,lazyValidation:Boolean},data:function(){return{inputs:[],watchers:[],errorBag:{}}},watch:{errorBag:{handler:function(t){var e=Object.values(t).includes(!0);this.$emit("input",!e)},deep:!0,immediate:!0}},methods:{watchInput:function(t){var e=this,i=function(t){return t.$watch("hasError",function(i){e.$set(e.errorBag,t._uid,i)},{immediate:!0})},n={_uid:t._uid,valid:function(){},shouldValidate:function(){}};return this.lazyValidation?n.shouldValidate=t.$watch("shouldValidate",function(a){a&&(e.errorBag.hasOwnProperty(t._uid)||(n.valid=i(t)))}):n.valid=i(t),n},validate:function(){return this.inputs.every(function(t){return t.validate(!0)})},reset:function(){this.inputs.forEach(function(t){return t.reset()}),this.resetErrorBag()},resetErrorBag:function(){var t=this;this.lazyValidation&&setTimeout(function(){t.errorBag={}},0)},resetValidation:function(){this.inputs.forEach(function(t){return t.resetValidation()}),this.resetErrorBag()},register:function(t){this.inputs.push(t),this.watchers.push(this.watchInput(t))},unregister:function(t){var e=this.inputs.find(function(e){return e._uid===t._uid});if(e){var i=this.watchers.find(function(t){return t._uid===e._uid});i&&(i.valid(),i.shouldValidate()),this.watchers=this.watchers.filter(function(t){return t._uid!==e._uid}),this.inputs=this.inputs.filter(function(t){return t._uid!==e._uid}),this.$delete(this.errorBag,e._uid)}}},render:function(t){var e=this;return t("form",{staticClass:"v-form",attrs:a({novalidate:!0},this.$attrs),on:{submit:function(t){return e.$emit("submit",t)}}},this.$slots.default)}})},"5eda":function(t,e,i){var n=i("5ca1"),a=i("8378"),r=i("79e5");t.exports=function(t,e){var i=(a.Object||{})[t]||Object[t],o={};o[t]=e(i),n(n.S+n.F*r(function(){i(1)}),"Object",o)}},"76f8":function(t,e,i){"use strict";i.r(e);var n=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-dialog",{attrs:{width:"500",value:!0,persistent:""}},[i("v-card",[i("v-toolbar",{attrs:{flat:"",color:"grey lighten-4"}},[i("v-toolbar-title",[t._v("Input Data Lokasi")])],1),i("v-card-text",[i("v-form",{ref:"form",model:{value:t.formValid,callback:function(e){t.formValid=e},expression:"formValid"}},[i("v-text-field",{attrs:{required:"",label:"Nama"},model:{value:t.item.nama,callback:function(e){t.$set(t.item,"nama",e)},expression:"item.nama"}}),i("v-text-field",{attrs:{required:"",label:"Alamat"},model:{value:t.item.alamat,callback:function(e){t.$set(t.item,"alamat",e)},expression:"item.alamat"}}),i("v-select",{attrs:{items:t.options.jabatan,label:"Jabatan"},model:{value:t.item.jabatan,callback:function(e){t.$set(t.item,"jabatan",e)},expression:"item.jabatan"}}),i("v-text-field",{attrs:{rules:[t.rules.required,t.rules.lokasiJabatan],label:"Lokasi Jabatan"},model:{value:t.item.lokasiJabatan,callback:function(e){t.$set(t.item,"lokasiJabatan",e)},expression:"item.lokasiJabatan"}}),i("v-text-field",{attrs:{rules:[t.rules.required,t.rules.latLong],label:"Latitude"},model:{value:t.item.latitude,callback:function(e){t.$set(t.item,"latitude",e)},expression:"item.latitude"}}),i("v-text-field",{attrs:{rules:[t.rules.required,t.rules.latLong],label:"Longitude"},model:{value:t.item.longitude,callback:function(e){t.$set(t.item,"longitude",e)},expression:"item.longitude"}})],1)],1),i("v-card-actions",[i("v-btn",{attrs:{outlined:"",dark:"",color:"blue"},on:{click:t.add}},[t._v("\n        Simpan\n      ")]),i("v-btn",{attrs:{outlined:"",dark:"",color:"pink"},on:{click:t.cancel}},[t._v("\n        Batal\n      ")])],1)],1)],1)},a=[],r=(i("8e6e"),i("ac6a"),i("456d"),i("bd86")),o=i("2b0e"),s=i("da7e"),c=i("0817"),l=i("ceee"),u=i("cd28");function d(t,e){var i=Object.keys(t);return Object.getOwnPropertySymbols&&i.push.apply(i,Object.getOwnPropertySymbols(t)),e&&(i=i.filter(function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable})),i}function f(t){for(var e=1;e<arguments.length;e++){var i=null!=arguments[e]?arguments[e]:{};e%2?d(i,!0).forEach(function(e){Object(r["a"])(t,e,i[e])}):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(i)):d(i).forEach(function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(i,e))})}return t}var h=o["a"].extend({name:"DataAdd",data:function(){return{item:Object(s["b"])(),options:{jabatan:["rt","rw"]},rules:{required:l["a"].required,latLong:l["a"].latLong,lokasiJabatan:l["a"].lokasiJabatan},formValid:!1}},methods:{add:function(){var t=this;this.$refs.form.validate()?c["b"].create(f({},this.item)).then(function(){u["a"].$emit("admin-data-reload"),t.$router.back()}):alert("Periksa kembali data yang anda input!")},cancel:function(){this.$router.back()}}}),v=h,b=i("2877"),m=i("6544"),p=i.n(m),g=i("8336"),w=i("b0af"),k=i("99d9"),y=i("169a"),O=i("4bd4"),x=i("b974"),j=i("8654"),$=i("71d9"),_=i("2a7f"),B=Object(b["a"])(v,n,a,!1,null,null,null);e["default"]=B.exports;p()(B,{VBtn:g["a"],VCard:w["a"],VCardActions:k["a"],VCardText:k["b"],VDialog:y["a"],VForm:O["a"],VSelect:x["a"],VTextField:j["a"],VToolbar:$["a"],VToolbarTitle:_["b"]})},"8e6e":function(t,e,i){var n=i("5ca1"),a=i("990b"),r=i("6821"),o=i("11e9"),s=i("f1ae");n(n.S,"Object",{getOwnPropertyDescriptors:function(t){var e,i,n=r(t),c=o.f,l=a(n),u={},d=0;while(l.length>d)i=c(n,e=l[d++]),void 0!==i&&s(u,e,i);return u}})},9093:function(t,e,i){var n=i("ce10"),a=i("e11e").concat("length","prototype");e.f=Object.getOwnPropertyNames||function(t){return n(t,a)}},"990b":function(t,e,i){var n=i("9093"),a=i("2621"),r=i("cb7c"),o=i("7726").Reflect;t.exports=o&&o.ownKeys||function(t){var e=n.f(r(t)),i=a.f;return i?e.concat(i(t)):e}},bd86:function(t,e,i){"use strict";i.d(e,"a",function(){return r});var n=i("85f2"),a=i.n(n);function r(t,e,i){return e in t?a()(t,e,{value:i,enumerable:!0,configurable:!0,writable:!0}):t[e]=i,t}},ceee:function(t,e,i){"use strict";var n=/[-]?[0-9]+[.][0-9]*$/,a=/[0-9][0-9]+$/;function r(t){return!!t||"Tidak boleh kosong"}function o(t){return n.test(t)||"invalid latitude/longitude"}function s(t){return a.test(t)||"invalid lokasi jabatan"}e["a"]={latLong:o,lokasiJabatan:s,required:r}},da7e:function(t,e,i){"use strict";i.d(e,"b",function(){return n}),i.d(e,"a",function(){return a});var n=function(){return{_id:"",nama:"",alamat:"",jabatan:"rt",lokasiJabatan:"01",longitude:0,latitude:0}},a=function(){return{_id:void 0,a:{longitude:0,latitude:0},b:{longitude:0,latitude:0},aId:void 0,bId:void 0,length:0}}},f1ae:function(t,e,i){"use strict";var n=i("86cc"),a=i("4630");t.exports=function(t,e,i){e in t?n.f(t,e,a(0,i)):t[e]=i}}}]);
//# sourceMappingURL=chunk-da735daa.dee1e046.js.map