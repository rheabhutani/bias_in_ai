"use strict";

(function() {

    window.addEventListener("load", init);
    // window.addEventListener("load", function(){setTimeout(displayutk, 7000)}());


    function init() {
        id("input").addEventListener("change", select);
        // window.addEventListener("load", setTimeout(displayutk, 5000));

    }

    function select() {
        // var dropdown = id("dropdown");
        // var value = dropdown.options[dropdown.selectedIndex].value;
        var value = id("input").value.substring(12)
        console.log(value)
        id("calculating").classList.remove("hidden");
        if (value === "utk.zip") {
            setTimeout(displayutk, 9000);
            //displayutk();
        } else if (value == "nist.zip") {
            setTimeout(displaynist, 7000);
            //displaynist();
        }
        id("utk-bias").classList.add("hidden");
        id("nist-bias").classList.add("hidden");
        // dropdown.onchange = value;
    }
    
    function displayutk() {
        id("nist").classList.add("hidden");
        id("utk").classList.remove("hidden");
        id("calculating").classList.add("hidden");
        id("utk-bias").classList.remove("hidden");
    }

    function displaynist() {
        id("utk").classList.add("hidden");
        id("nist").classList.remove("hidden");
        id("calculating").classList.add("hidden");
        id("nist-bias").classList.remove("hidden");
    }
})();

// ------------------------- HELPER FUNCTIONS ------------------------- //
  /**
   * Returns the element that has the ID attribute with the specified value.
   * @param {string} idName - element ID.
   * @return {object} DOM object associated with id.
   */
   function id(idName) {
    return document.getElementById(idName);
  }

  /**
   * Returns a new element with the given tag name.
   * @param {string} tagName - HTML tag name for new DOM element.
   * @returns {object} New DOM object for given HTML tag.
   */
  function gen(tagName) {
    return document.createElement(tagName);
  }

  /**
   * Returns the first element that matches the given CSS selector.
   * @param {string} selector - CSS query selector.
   * @returns {object} The first DOM object matching the query.
   */
   function qs(selector) {
    return document.querySelector(selector);
  }

  /**
   * Returns the array of elements that match the given CSS selector.
   * @param {string} selector - CSS query selector
   * @returns {object[]} array of DOM objects matching the query.
   */
  function qsa(selector) {
    return document.querySelectorAll(selector);
  }