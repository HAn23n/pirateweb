$(document).ready(function() {
	$('#random-btn').click(function() {
		$.ajax({
			url: "{% url 'random' %}",
			type: "GET",
			success: function(data) {
				if (data.error) {
					alert(data.error);
				} else {
					$('#stamina').text(data.stamina);
					$('#heal').text(data.heal);
					$('#skill').text(data.skill);
					$('#rank').text(data.rank);
					$('#total').text(data.total);
					$('#random-btn').hide();
					$('#random').append('<div class="text-center mt-3"><button class="btn" id="next-btn" onclick="showNextBox()">Next</button></div>');
				}
			}
		});
	});
});

function showNextBox() {
	var wrapper = document.getElementById('wrapper');
	var nextBox = document.getElementById('next-box');
	var randomBtn = document.getElementById('random-btn');

	wrapper.style.display = 'none';
	nextBox.style.display = 'block';

	$('#rank_c').text($('#rank').text());
	$('#stamina_c').text($('#stamina').text());
	$('#heal_c').text($('#heal').text());
	$('#skill_c').text($('#skill').text());
	$('#total_c').text($('#total').text());


	randomBtn.textContent = 'Next';
}
