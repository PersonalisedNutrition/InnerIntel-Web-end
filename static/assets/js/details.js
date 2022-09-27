$(".detail").on('click',function(event) {
	var type = $(this).attr("data-type");

	$(".detail"+type).toggle();
	var $this=$(this);
	if($this.hasClass('unclick')){
		$this.removeClass('unclick').addClass('click');
	}else{
		$this.removeClass('click').addClass('unclick');
	}
});

