"use strict";

(function() {
    window.addEventListener("load", init);
    
    function init() {
        id("input3").addEventListener("change", select);
    }

    function select() {
        id("plots").classList.add("hidden")
        id("calculating").classList.remove("hidden");
        setTimeout(display, 10000)
    }

    function display() {
        id("calculating").classList.add("hidden");
        id("plots").classList.remove("hidden")
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