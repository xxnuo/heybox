import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.3770.100 Safari/537.36"
}
import json
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    html_body = ""
    html_body_raw = """
		<article class="white-panel">
			<div>
				<img src="{}" class="thumb">
				<span class="user">{}</span>
				<span class="time">刚刚</span>
			</div>
			<h1><a href="{}" target="_blank">{}</a></h1>
			<div>
				<span class="tip"> ID </span><span class="bungie_id">{}</span>
				<span class="tip"> 光等 </span><span class="req_guan">{}</span>
			</div>
		</article>

"""
    heyUrl = "https://api.xiaoheihe.cn/game/h5_activity/common_team/data?appid=1085660&need_list=1&offset=0&limit=30"
    _response = requests.get(heyUrl, headers=headers)
    data = json.loads(_response.text)

    trimData = data["result"]["data_list"]
    for singleData in trimData:
        try:
            username = singleData["user"]["username"]
            avatar = singleData["user"]["avatar"]
            team_text = singleData["team_data"]["team_text"]
            share_url = singleData["share_url"]
            bungie_id = singleData["team_data"]["name"]["value"]
            req_guang = singleData["team_data"]["guang"]["value"]
            # description = singleData["description"]
        except Exception:
            pass
        if bungie_id == "":
            bungie_id = "无"
        if req_guang == "":
            req_guang = "无"
        html_body += html_body_raw.format(
            avatar, username, share_url, team_text, bungie_id, req_guang
        )

    return html_head + html_body + html_end


# 上面的html_body格式化的模板
html_body_template = """
		<article class="white-panel">
			<div>
				<img src="{user_avatar}" class="thumb">
				<span class="user">{username}</span>
				<span class="time">刚刚</span>
			</div>
			<h1><a href="{share_url}" target="_blank">{team_text}</a></h1>
			<div>
				<span class="tip"> ID </span><span class="bungie_id">{bungie_id}</span>
				<span class="tip"> 光等 </span><span class="req_guan">{req_guang}</span>
			</div>
		</article>

"""
html_head = """
<!DOCTYPE html>
<html lang="Zh-CN">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>组队</title>
	<!-- normalize.css -->
	<style type="text/css">
		article,
		aside,
		details,
		figcaption,
		figure,
		footer,
		header,
		hgroup,
		main,
		nav,
		section,
		summary {
			display: block;
		}

		audio,
		canvas,
		video {
			display: inline-block;
		}

		audio:not([controls]) {
			display: none;
			height: 0;
		}

		[hidden] {
			display: none;
		}

		html {
			font-family: sans-serif;
			-ms-text-size-adjust: 100%;
			-webkit-text-size-adjust: 100%;
		}

		body {
			margin: 0;
		}

		a:focus {
			outline: thin dotted;
		}

		a:active,
		a:hover {
			outline: 0;
		}

		h1 {
			font-size: 2em;
			margin: 0.67em 0;
		}

		abbr[title] {
			border-bottom: 1px dotted;
		}

		b,
		strong {
			font-weight: bold;
		}

		dfn {
			font-style: italic;
		}

		hr {
			-moz-box-sizing: content-box;
			box-sizing: content-box;
			height: 0;
		}

		mark {
			background: #ff0;
			color: #000;
		}

		code,
		kbd,
		pre,
		samp {
			font-family: monospace, serif;
			font-size: 1em;
		}

		pre {
			white-space: pre-wrap;
		}

		q {
			quotes: "\201C""\201D""\2018""\2019";
		}

		small {
			font-size: 80%;
		}

		sub,
		sup {
			font-size: 75%;
			line-height: 0;
			position: relative;
			vertical-align: baseline;
		}

		sup {
			top: -0.5em;
		}

		sub {
			bottom: -0.25em;
		}

		img {
			border: 0;
		}

		svg:not(:root) {
			overflow: hidden;
		}

		figure {
			margin: 0;
		}

		fieldset {
			border: 1px solid #c0c0c0;
			margin: 0 2px;
			padding: 0.35em 0.625em 0.75em;
		}

		legend {
			border: 0;
			padding: 0;
		}

		button,
		input,
		select,
		textarea {
			font-family: inherit;
			font-size: 100%;
			margin: 0;
		}

		button,
		input {
			line-height: normal;
		}

		button,
		select {
			text-transform: none;
		}

		button,
		html input[type="button"],
		input[type="reset"],
		input[type="submit"] {
			-webkit-appearance: button;
			cursor: pointer;
		}

		button[disabled],
		html input[disabled] {
			cursor: default;
		}

		input[type="checkbox"],
		input[type="radio"] {
			box-sizing: border-box;
			padding: 0;
		}

		input[type="search"] {
			-webkit-appearance: textfield;
			-moz-box-sizing: content-box;
			-webkit-box-sizing: content-box;
			box-sizing: content-box;
		}

		input[type="search"]::-webkit-search-cancel-button,
		input[type="search"]::-webkit-search-decoration {
			-webkit-appearance: none;
		}

		button::-moz-focus-inner,
		input::-moz-focus-inner {
			border: 0;
			padding: 0;
		}

		textarea {
			overflow: auto;
			vertical-align: top;
		}

		table {
			border-collapse: collapse;
			border-spacing: 0;
		}
	</style>
	<!-- default.css -->
	<style type="text/css">
		/*@import url(http://fonts.useso.com/css?family=Raleway:200,500,700,800);*/
		@font-face {
			font-family: 'icomoon';
			src: url('../fonts/icomoon.eot?rretjt');
			src: url('../fonts/icomoon.eot?#iefixrretjt') format('embedded-opentype'),
				url('../fonts/icomoon.woff?rretjt') format('woff'),
				url('../fonts/icomoon.ttf?rretjt') format('truetype'),
				url('../fonts/icomoon.svg?rretjt#icomoon') format('svg');
			font-weight: normal;
			font-style: normal;
		}

		[class^="icon-"],
		[class*=" icon-"] {
			font-family: 'icomoon';
			speak: none;
			font-style: normal;
			font-weight: normal;
			font-variant: normal;
			text-transform: none;
			line-height: 1;

			/* Better Font Rendering =========== */
			-webkit-font-smoothing: antialiased;
			-moz-osx-font-smoothing: grayscale;
		}

		body,
		html {
			font-size: 100%;
			padding: 0;
			margin: 0;
		}

		/* Reset */
		*,
		*:after,
		*:before {
			-webkit-box-sizing: border-box;
			-moz-box-sizing: border-box;
			box-sizing: border-box;
		}

		/* Clearfix hack by Nicolas Gallagher: http://nicolasgallagher.com/micro-clearfix-hack/ */
		.clearfix:before,
		.clearfix:after {
			content: " ";
			display: table;
		}

		.clearfix:after {
			clear: both;
		}

		body {
			background: #494A5F;
			/* 卡片文字色 */
			color: #000000;
			font-weight: 500;
			font-size: 1.05em;
			font-family: "Microsoft YaHei", "宋体", "Segoe UI", "Lucida Grande", Helvetica, Arial, sans-serif, FreeSans, Arimo;
		}

		a {
			color: #2fa0ec;
			text-decoration: none;
			outline: none;
		}

		a:hover,
		a:focus {
			color: #74777b;
		}

		.htmleaf-container {
			margin: 0 auto;
			text-align: center;
			overflow: hidden;
		}

		.htmleaf-content {
			font-size: 150%;
			padding: 1em 0;
		}

		.htmleaf-content h2 {
			margin: 0 0 2em;
			opacity: 0.1;
		}

		.htmleaf-content p {
			margin: 1em 0;
			padding: 5em 0 0 0;
			font-size: 0.65em;
		}

		.bgcolor-1 {
			background: #f0efee;
		}

		.bgcolor-2 {
			background: #f9f9f9;
		}

		.bgcolor-3 {
			background: #e8e8e8;
		}

		/*light grey*/
		.bgcolor-4 {
			background: #2f3238;
			color: #fff;
		}

		/*Dark grey*/
		.bgcolor-5 {
			background: #df6659;
			color: #521e18;
		}

		/*pink1*/
		.bgcolor-6 {
			background: #2fa8ec;
		}

		/*sky blue*/
		.bgcolor-7 {
			background: #d0d6d6;
		}

		/*White tea*/
		.bgcolor-8 {
			background: #3d4444;
			color: #fff;
		}

		/*Dark grey2*/
		.bgcolor-9 {
			background: #ef3f52;
			color: #fff;
		}

		/*pink2*/
		.bgcolor-10 {
			background: #64448f;
			color: #fff;
		}

		/*Violet*/
		.bgcolor-11 {
			background: #3755ad;
			color: #fff;
		}

		/*dark blue*/
		.bgcolor-12 {
			background: #3498DB;
			color: #fff;
		}

		/*light blue*/
		.bgcolor-20 {
			background: #494A5F;
			color: #D5D6E2;
		}

		/* Header */
		.htmleaf-header {
			padding: 1em 190px 1em;
			letter-spacing: -1px;
			text-align: center;
			background: #66677c;
		}

		.htmleaf-header h1 {
			color: #D5D6E2;
			font-weight: 600;
			font-size: 2em;
			line-height: 1;
			margin-bottom: 0;
			font-family: "Microsoft YaHei", "宋体", "Segoe UI", "Lucida Grande", Helvetica, Arial, sans-serif, FreeSans, Arimo;
		}

		.htmleaf-header h1 span {
			font-family: "Microsoft YaHei", "宋体", "Segoe UI", "Lucida Grande", Helvetica, Arial, sans-serif, FreeSans, Arimo;
			display: block;
			font-size: 60%;
			font-weight: 400;
			padding: 0.8em 0 0.5em 0;
			color: #c3c8cd;
		}

		/*nav*/
		.htmleaf-demo a {
			color: #1d7db1;
			text-decoration: none;
		}

		.htmleaf-demo {
			width: 100%;
			padding-bottom: 1.2em;
		}

		.htmleaf-demo a {
			display: inline-block;
			margin: 0.5em;
			padding: 0.6em 1em;
			border: 3px solid #1d7db1;
			font-weight: 700;
		}

		.htmleaf-demo a:hover {
			opacity: 0.6;
		}

		.htmleaf-demo a.current {
			background: #1d7db1;
			color: #fff;
		}

		/* Top Navigation Style */
		.htmleaf-links {
			position: relative;
			display: inline-block;
			white-space: nowrap;
			font-size: 1.5em;
			text-align: center;
		}

		.htmleaf-links::after {
			position: absolute;
			top: 0;
			left: 50%;
			margin-left: -1px;
			width: 2px;
			height: 100%;
			background: #dbdbdb;
			content: '';
			-webkit-transform: rotate3d(0, 0, 1, 22.5deg);
			transform: rotate3d(0, 0, 1, 22.5deg);
		}

		.htmleaf-icon {
			display: inline-block;
			margin: 0.5em;
			padding: 0em 0;
			width: 1.5em;
			text-decoration: none;
		}

		.htmleaf-icon span {
			display: none;
		}

		.htmleaf-icon:before {
			margin: 0 5px;
			text-transform: none;
			font-weight: normal;
			font-style: normal;
			font-variant: normal;
			font-family: 'icomoon';
			line-height: 1;
			speak: none;
			-webkit-font-smoothing: antialiased;
		}

		/* footer */
		.htmleaf-footer {
			width: 100%;
			padding-top: 10px;
		}

		.htmleaf-small {
			font-size: 0.8em;
		}

		.center {
			text-align: center;
		}

		/****/
		.related {
			color: #fff;
			background: #494A5F;
			text-align: center;
			font-size: 1.25em;
			padding: 0.5em 0;
			overflow: hidden;
		}

		.related>a {
			vertical-align: top;
			width: calc(100% - 20px);
			max-width: 340px;
			display: inline-block;
			text-align: center;
			margin: 20px 10px;
			padding: 25px;
			font-family: "Microsoft YaHei", "宋体", "Segoe UI", "Lucida Grande", Helvetica, Arial, sans-serif, FreeSans, Arimo;
		}

		.related a {
			display: inline-block;
			text-align: left;
			margin: 20px auto;
			padding: 10px 20px;
			opacity: 0.8;
			-webkit-transition: opacity 0.3s;
			transition: opacity 0.3s;
			-webkit-backface-visibility: hidden;
		}

		.related a:hover,
		.related a:active {
			opacity: 1;
		}

		.related a img {
			max-width: 100%;
			opacity: 0.8;
			border-radius: 4px;
		}

		.related a:hover img,
		.related a:active img {
			opacity: 1;
		}

		.related h3 {
			font-family: "Microsoft YaHei", sans-serif;
		}

		.related a h3 {
			font-weight: 300;
			margin-top: 0.15em;
			color: #fff;
		}

		/* icomoon */
		.icon-htmleaf-home-outline:before {
			content: "\e5000";
		}

		.icon-htmleaf-arrow-forward-outline:before {
			content: "\e5001";
		}

		@media screen and (max-width: 50em) {
			.htmleaf-header {
				padding: 3em 10% 4em;
			}

			.htmleaf-header h1 {
				font-size: 2em;
			}
		}


		@media screen and (max-width: 40em) {
			.htmleaf-header h1 {
				font-size: 1.5em;
			}
		}

		@media screen and (max-width: 30em) {
			.htmleaf-header h1 {
				font-size: 1.2em;
			}
		}
	</style>

	<style type="text/css">
		#gallery-wrapper {
			position: relative;
			max-width: 75%;
			width: 75%;
			margin: 50px auto;
		}

		/* 头像图片设置 */
		img.thumb {
			height: 40px;
			width: 40px;
			border-radius: 40px;
		}

		span.user {
			position: absolute;
			margin-left: 5px;
		}

		span.time {
			position: absolute;
			margin-top: 20px;
			margin-left: 5px;
			font-size: 8px;
		}

		span.tip {
			font-size: small;
		}

		.white-panel {
			position: absolute;
			background: white;
			border-radius: 5px;
			box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.3);
			padding: 10px;
		}

		.white-panel h1 {
			font-size: 1em;
		}

		.white-panel h1 a {
			color: #A92733;
		}

		.white-panel:hover {
			box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.5);
			margin-top: -5px;
			-webkit-transition: all 0.3s ease-in-out;
			-moz-transition: all 0.3s ease-in-out;
			-o-transition: all 0.3s ease-in-out;
			transition: all 0.3s ease-in-out;
		}
	</style>
	<!--[if IE]>
		<script src="https://cdn.staticfile.org/html5shiv/3.7.2/html5shiv.min.js"></script>
	<![endif]-->
</head>

<body>

	<section id="gallery-wrapper">

"""

html_end = """

	</section>

	<script src="https://cdn.staticfile.org/jquery/3.4.1/jquery.min.js"></script>
	<!-- pinterest_grid.js -->
	<script type="text/javascript">
		/*
	Pinterest Grid Plugin
	Copyright 2014 Mediademons
	@author smm 16/04/2014

	usage:

	 $(document).ready(function() {

		$('#blog-landing').pinterest_grid({
			no_columns: 4
		});

	});
	*/
		; (function ($, window, document, undefined) {
			var pluginName = 'pinterest_grid',
				defaults = {
					padding_x: 10,
					padding_y: 10,
					no_columns: 3,
					margin_bottom: 50,
					single_column_breakpoint: 700
				},
				columns,
				$article,
				article_width;

			function Plugin(element, options) {
				this.element = element;
				this.options = $.extend({}, defaults, options);
				this._defaults = defaults;
				this._name = pluginName;
				this.init();
			}

			Plugin.prototype.init = function () {
				var self = this,
					resize_finish;

				$(window).resize(function () {
					clearTimeout(resize_finish);
					resize_finish = setTimeout(function () {
						self.make_layout_change(self);
					}, 11);
				});

				self.make_layout_change(self);

				setTimeout(function () {
					$(window).resize();
				}, 500);
			};

			Plugin.prototype.calculate = function (single_column_mode) {
				var self = this,
					tallest = 0,
					row = 0,
					$container = $(this.element),
					container_width = $container.width();
				$article = $(this.element).children();

				if (single_column_mode === true) {
					article_width = $container.width() - self.options.padding_x;
				} else {
					article_width = ($container.width() - self.options.padding_x * self.options.no_columns) / self.options.no_columns;
				}

				$article.each(function () {
					$(this).css('width', article_width);
				});

				columns = self.options.no_columns;

				$article.each(function (index) {
					var current_column,
						left_out = 0,
						top = 0,
						$this = $(this),
						prevAll = $this.prevAll(),
						tallest = 0;

					if (single_column_mode === false) {
						current_column = (index % columns);
					} else {
						current_column = 0;
					}

					for (var t = 0; t < columns; t++) {
						$this.removeClass('c' + t);
					}

					if (index % columns === 0) {
						row++;
					}

					$this.addClass('c' + current_column);
					$this.addClass('r' + row);

					prevAll.each(function (index) {
						if ($(this).hasClass('c' + current_column)) {
							top += $(this).outerHeight() + self.options.padding_y;
						}
					});

					if (single_column_mode === true) {
						left_out = 0;
					} else {
						left_out = (index % columns) * (article_width + self.options.padding_x);
					}

					$this.css({
						'left': left_out,
						'top': top
					});
				});

				this.tallest($container);
				$(window).resize();
			};

			Plugin.prototype.tallest = function (_container) {
				var column_heights = [],
					largest = 0;

				for (var z = 0; z < columns; z++) {
					var temp_height = 0;
					_container.find('.c' + z).each(function () {
						temp_height += $(this).outerHeight();
					});
					column_heights[z] = temp_height;
				}

				largest = Math.max.apply(Math, column_heights);
				_container.css('height', largest + (this.options.padding_y + this.options.margin_bottom));
			};

			Plugin.prototype.make_layout_change = function (_self) {
				if ($(window).width() < _self.options.single_column_breakpoint) {
					_self.calculate(true);
				} else {
					_self.calculate(false);
				}
			};

			$.fn[pluginName] = function (options) {
				return this.each(function () {
					if (!$.data(this, 'plugin_' + pluginName)) {
						$.data(this, 'plugin_' + pluginName,
							new Plugin(this, options));
					}
				});
			}

		})(jQuery, window, document);
	</script>

	<script type="text/javascript">
		$(function () {
			$("#gallery-wrapper").pinterest_grid({
				no_columns: 4,
				padding_x: 10,
				padding_y: 10,
				margin_bottom: 50,
				single_column_breakpoint: 700
			});

		});
	</script>
</body>

</html>
"""

if __name__ == "__main__":
    app.run()
