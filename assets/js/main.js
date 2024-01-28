function show_video_player(){
    $('#video-start-icon').css('display', 'none');
    $('#video-over-info').css('display', 'none');
    $('#video-player').load();
    $('#video-player').attr('controls',true);
    $('#video-player').get(0).play();
}