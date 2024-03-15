import { FormEvent, useEffect, useState } from 'react'

export default function index() {
    const [hasApiKey, setHasApiKey] = useState(true);
    useEffect(() => {
        const apiKey = localStorage.getItem('apiKey');
        if(!apiKey) {
            setHasApiKey(false);
        }
    }, []);

    const onSubmit = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        console.log(e.target.elements.apiKey.value);
    }

    return (
        <>
            {hasApiKey ? 
                <></>
            : 
                <div className={`api-key-checker ${hasApiKey ? 'api-key-checker--closed' : ''}`}> 
                    <div className='api-key-checker__inner'>
                        {/* possibly a separated component */}
                        <form className="api-key-checker__form" onSubmit={onSubmit}>
                            <p>Please enter your API key in the settings</p>
                            <input type="text" placeholder="API key" name='apiKey'/>
                            <button type="submit">Use this api key</button>
                        </form>
                    </div>
                </div>
            }
        </>
    )
}
