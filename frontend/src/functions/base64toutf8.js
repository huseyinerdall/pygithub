function base64toutf8(str) {
    return decodeURIComponent(escape(window.atob( str )));
}

module.exports = base64toutf8