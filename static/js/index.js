require.config({ paths: { 'vs': 'https://unpkg.com/monaco-editor@latest/min/vs' } });
window.MonacoEnvironment = { getWorkerUrl: () => proxy };
let proxy = URL.createObjectURL(new Blob([`
	self.MonacoEnvironment = {
		baseUrl: 'https://unpkg.com/monaco-editor@latest/min/'
	};
	importScripts('https://unpkg.com/monaco-editor@latest/min/vs/base/worker/workerMain.js');
`], { type: 'text/javascript' }));

var model = require(["vs/editor/editor.main"], function () {
	let editor = monaco.editor.create(document.getElementById('editor'), {
		value: 
			'#Python \n # \u2193 \u2193 Code here \u2193 \u2193 \n #clear this if any other langauge',
		language: 'python',
		theme: 'vs-dark'
	});
	async function save() {
		// get the value of the data
		var value = editor.getValue();
		$.post("/getcode", {
			javascript_data: value,
			success: setTimeout(function () {
				var output = document.getElementById("output");
				$.ajax({
					url: "/outputcode",
					type: "post",
					success: function(response) {
					  output.innerHTML = response;
					 },
					error: function(xhr) {
						//Handel error
					}
				  });
			}, 2000),
			error: function (xhr) {
				//Handel error
			}
		},);
	};
	/*async function display() 
	{const res = await $.ajax({
				url: "/outputcode",
				type: "post",
				success: function(response) {
				  output.innerHTML = response;
				 },
				error: function(xhr) {
					//Handel error
				}
			  });
			return res;
			} */

	document.getElementById('save_code').onclick = save;
});