from modules import launch_utils 
IllIIlIIlIllllllI =launch_utils .args 
IlIllIlIIllIllIlI =launch_utils .python 
IIIIIIIllIIlIIllI =launch_utils .git 
IIlIIIllIllIIIIII =launch_utils .index_url 
IlIIIIIIIIIlIIIIl =launch_utils .dir_repos 
IllIIIlllIlllllll =launch_utils .commit_hash 
IlIllIIlIIIllllll =launch_utils .git_tag 
IIlIlIIlIIlIlIlII =launch_utils .run 
IIIIllIIIllllIIIl =launch_utils .is_installed 
IlIllIIIlIIllIllI =launch_utils .repo_dir 
IIllllllllIIIllIl =launch_utils .run_pip 
IllIlIllIllIllIll =launch_utils .check_run_python 
IlllIIlllIIlIIllI =launch_utils .git_clone 
IIllllIIIIIIlIlll =launch_utils .git_pull_recursive 
IlIlIlllIlIllIIII =launch_utils .list_extensions 
IlllIIIIIIIlllIlI =launch_utils .run_extension_installer 
IIlIlIllIIlIIIllI =launch_utils .prepare_environment 
IllIIIllllIIIlIlI =launch_utils .configure_for_tests 
IlllIlIllIlllIlIl =launch_utils .start 
def IllIIllIlIIIIIlIl ():
	if IllIIlIIlIllllllI .dump_sysinfo :IlIlllIIIIIIIlllI =launch_utils .dump_sysinfo ();print (f"Sysinfo saved as {IlIlllIIIIIIIlllI}. Exiting...");exit (0 )
	launch_utils .startup_timer .record ('initial startup')
	with launch_utils .startup_timer .subcategory ('prepare environment'):
		if not IllIIlIIlIllllllI .skip_prepare_environment :IIlIlIllIIlIIIllI ()
	if IllIIlIIlIllllllI .test_server :IllIIIllllIIIlIlI ()
	IlllIlIllIlllIlIl ()
if __name__ =='__main__':IllIIllIlIIIIIlIl ()
